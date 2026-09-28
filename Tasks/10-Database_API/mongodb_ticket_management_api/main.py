from fastapi import FastAPI, HTTPException
from database import collection
from models import TicketCreate, TicketUpdate, StatusUpdate, Comment
from datetime import datetime

# Create a FastAPI instance
app = FastAPI()

# Create new ticket Endpoint
@app.post("/tickets")
def create_ticket(ticket: TicketCreate):
    max_ticket_id = collection.find_one(sort=[("_id", -1)])["_id"] if collection.count_documents({}) > 0 else 0
    ticket_id = max_ticket_id + 1
    ticket_dict = ticket.model_dump(exclude_unset=True)
    ticket_dict["_id"] = ticket_id
    ticket_dict["status"] = "Open"
    ticket_dict["created_at"] = datetime.now().isoformat()
    ticket_dict["updated_at"] = datetime.now().isoformat()
    collection.insert_one(ticket_dict)
    return {"ticket_id": ticket_id, "message": "Ticket created successfully."}

# Get all tickets Endpoint
@app.get("/tickets")
def get_tickets():
    tickets = list(collection.find())
    for ticket in tickets:
        ticket["_id"] = str(ticket["_id"])
    return tickets

# Update ticket Endpoint
@app.patch("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, ticket_update: TicketUpdate):
    ticket_dict = ticket_update.model_dump(exclude_unset=True)
    if not ticket_dict:
        raise HTTPException(status_code=400, detail="No fields provided for update.")
    ticket_dict["updated_at"] = datetime.now().isoformat()
    result = collection.update_one({"_id": ticket_id}, {"$set": ticket_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Ticket not found.")
    return {"message": "Ticket updated successfully."}


# Add comment to ticket Endpoint
@app.post("/tickets/{ticket_id}/comments")
def add_comment(ticket_id: int, comment: Comment):
    comment_dict = comment.model_dump(exclude_unset=True)
    comment_dict["created_at"] = datetime.now().isoformat()
    result = collection.update_one({"_id": ticket_id}, {"$push": {"comments": comment_dict}, "$set": {"updated_at": datetime.now().isoformat()}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Ticket not found.")
    return {"message": "Comment added successfully."}


# Update ticket status Endpoint
@app.patch("/tickets/{ticket_id}/status")
def update_ticket_status(ticket_id: int, status_update: StatusUpdate):
    result = collection.update_one({"_id": ticket_id}, {"$set": {"status": status_update.status, "updated_at": datetime.now().isoformat()}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Ticket not found.")
    return {"message": "Ticket status updated successfully."}



# Filter tickets by priority/status Endpoint
@app.get("/tickets/filter")
def filter_tickets(status: str, priority: str = None):
    query = {"status": status}
    if priority:
        query["priority"] = priority
    tickets = list(collection.find(query))
    if not tickets:
        raise HTTPException(status_code=404, detail="No tickets found with the specified status.")
    return tickets


# Get ticket by ID Endpoint
@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    ticket = collection.find_one({"_id": ticket_id})
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found.")
    return ticket


# Delete ticket Endpoint
@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    result = collection.delete_one({"_id": ticket_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Ticket not found.")
    return {"message": "Ticket deleted successfully."}