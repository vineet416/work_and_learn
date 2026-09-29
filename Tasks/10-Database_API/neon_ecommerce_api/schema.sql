-- ==========================================
-- E-COMMERCE DATABASE SCHEMA
-- ==========================================


-- ==========================================
-- USERS TABLE
-- ==========================================

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);


-- ==========================================
-- PRODUCTS TABLE
-- ==========================================

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    inventory INTEGER NOT NULL DEFAULT 0 CHECK (inventory >= 0)
);


-- ==========================================
-- ORDERS TABLE
-- ==========================================

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,

    user_id INTEGER NOT NULL,

    status VARCHAR(20) NOT NULL DEFAULT 'placed',

    total_amount NUMERIC(10, 2) NOT NULL DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_orders_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
);


-- ==========================================
-- ORDER ITEMS TABLE
-- ==========================================

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,

    order_id INTEGER NOT NULL,

    product_id INTEGER NOT NULL,

    quantity INTEGER NOT NULL CHECK (quantity > 0),

    unit_price NUMERIC(10, 2) NOT NULL,

    item_total NUMERIC(10, 2) NOT NULL,

    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id)
        REFERENCES orders(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_order_items_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
);