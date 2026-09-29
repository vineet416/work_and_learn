from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from database import SessionLocal
from models import UserCreate, InventoryUpdate, OrderCreate

# FastAPI app instance
app = FastAPI()

# 1. CREATE USER ACCOUNT
@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()
    try:
        result = db.execute(text("INSERT INTO users (name, email) VALUES (:name, :email) RETURNING id, name, email"), 
                            {"name": user.name, "email": user.email})
        new_user = result.fetchone()
        db.commit()
        return {"id": new_user.id, "name": new_user.name, "email": new_user.email}
    finally:
        db.close()


# 2. VIEW PRODUCTS
@app.get("/products")
def view_products():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT id, name, price, inventory FROM products ORDER BY id"))
        products = result.fetchall()
        return [
            {"id": product.id, "name": product.name, "price": float(product.price), "inventory": product.inventory}
            for product in products
        ]
    finally:
        db.close()


# 3. PLACE AN ORDER
@app.post("/orders")
def place_order(order: OrderCreate):
    db = SessionLocal()
    try:
        # Check whether user exists
        user = db.execute(text("SELECT id FROM users WHERE id = :user_id"), {"user_id": order.user_id}).fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        # Check whether order contains items
        if not order.items:
            raise HTTPException(status_code=400, detail="Order must contain at least one product")
        # Create order
        order_result = db.execute(
            text("""
                INSERT INTO orders
                (
                    user_id,
                    status,
                    total_amount
                )
                VALUES
                (
                    :user_id,
                    'placed',
                    0
                )
                RETURNING id
            """),
            {"user_id": order.user_id},
        )
        order_id = order_result.fetchone().id
        order_total = 0
        # Process each product
        for item in order.items:
            product = db.execute(
                text("""
                    SELECT
                        id,
                        name,
                        price,
                        inventory
                    FROM products
                    WHERE id = :product_id
                """),
                {"product_id": item.product_id},
            ).fetchone()
            if not product:
                raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
            # Check inventory
            if product.inventory < item.quantity:
                raise HTTPException(status_code=400, detail=f"Not enough inventory for {product.name}")
            # Quantity × Unit Price = Item Total
            item_total = item.quantity * float(product.price)
            # Insert order item
            db.execute(
                text("""
                    INSERT INTO order_items
                    (
                        order_id,
                        product_id,
                        quantity,
                        unit_price,
                        item_total
                    )
                    VALUES
                    (
                        :order_id,
                        :product_id,
                        :quantity,
                        :unit_price,
                        :item_total
                    )
                """),
                {
                    "order_id": order_id,
                    "product_id": product.id,
                    "quantity": item.quantity,
                    "unit_price": product.price,
                    "item_total": item_total,
                },
            )
            # Reduce product inventory
            db.execute(
                text("""
                    UPDATE products
                    SET inventory = inventory - :quantity
                    WHERE id = :product_id
                """),
                {"quantity": item.quantity, "product_id": item.product_id},
            )
            # Add item total to order total
            order_total += item_total
        # Update final order total
        db.execute(
            text("""
                UPDATE orders
                SET total_amount = :total_amount
                WHERE id = :order_id
            """),
            {"total_amount": order_total, "order_id": order_id},
        )
        db.commit()
        return {"message": "Order placed successfully", "order_id": order_id, "order_total": order_total}
    except HTTPException:
        db.rollback()
        raise
    finally:
        db.close()


# 4. VIEW USER'S ORDERS
@app.get("/users/{user_id}/orders")
def view_user_orders(user_id: int):
    db = SessionLocal()
    try:
        # JOIN + WHERE + ORDER BY
        result = db.execute(
            text("""
                SELECT
                    o.id AS order_id,
                    o.user_id,
                    o.status,
                    o.total_amount,
                    oi.product_id,
                    p.name AS product_name,
                    oi.quantity,
                    oi.unit_price,
                    oi.item_total
                FROM orders o
                JOIN order_items oi
                    ON o.id = oi.order_id
                JOIN products p
                    ON oi.product_id = p.id
                WHERE o.user_id = :user_id
                ORDER BY o.id DESC
            """),
            {"user_id": user_id},
        )
        rows = result.fetchall()
        if not rows:
            return []
        orders = {}
        for row in rows:
            if row.order_id not in orders:
                orders[row.order_id] = {
                    "order_id": row.order_id,
                    "user_id": row.user_id,
                    "status": row.status,
                    "order_total": float(row.total_amount),
                    "items": [],
                }
            orders[row.order_id]["items"].append(
                {
                    "product_id": row.product_id,
                    "product_name": row.product_name,
                    "quantity": row.quantity,
                    "unit_price": float(row.unit_price),
                    "item_total": float(row.item_total),
                }
            )
        return list(orders.values())
    finally:
        db.close()


# 5. UPDATE PRODUCT INVENTORY
@app.put("/products/{product_id}/inventory")
def update_product_inventory(product_id: int, inventory_data: InventoryUpdate):
    db = SessionLocal()
    try:
        # Check product
        product = db.execute(
            text("""
                SELECT id
                FROM products
                WHERE id = :product_id
            """),
            {"product_id": product_id},
        ).fetchone()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        # Update inventory
        db.execute(
            text("""
                UPDATE products
                SET inventory = :inventory
                WHERE id = :product_id
            """),
            {"inventory": inventory_data.inventory, "product_id": product_id},
        )
        db.commit()
        return {
            "message": "Product inventory updated successfully",
            "product_id": product_id,
            "inventory": inventory_data.inventory,
        }
    finally:
        db.close()


# 6. CANCEL AN ORDER
@app.put("/orders/{order_id}/cancel")
def cancel_order(order_id: int):
    db = SessionLocal()
    try:
        # Find order
        order = db.execute(
            text("""
                SELECT
                    id,
                    status
                FROM orders
                WHERE id = :order_id
            """),
            {"order_id": order_id},
        ).fetchone()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        if order.status == "cancelled":
            raise HTTPException(status_code=400, detail="Order is already cancelled")
        # Get order items
        items = db.execute(
            text("""
                SELECT
                    product_id,
                    quantity
                FROM order_items
                WHERE order_id = :order_id
            """),
            {"order_id": order_id},
        ).fetchall()
        # Return products to inventory
        for item in items:
            db.execute(
                text("""
                    UPDATE products
                    SET inventory = inventory + :quantity
                    WHERE id = :product_id
                """),
                {"quantity": item.quantity, "product_id": item.product_id},
            )
        # Change order status
        db.execute(
            text("""
                UPDATE orders
                SET status = 'cancelled'
                WHERE id = :order_id
            """),
            {"order_id": order_id},
        )
        db.commit()
        return {"message": "Order cancelled successfully", "order_id": order_id, "status": "cancelled"}
    except HTTPException:
        db.rollback()
        raise
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Could not cancel order")
    finally:
        db.close()