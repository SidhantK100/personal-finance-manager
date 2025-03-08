from fastapi import FastAPI, HTTPException
from app.utils.database import db, client  # Import centralized database connection
from bson import ObjectId

app = FastAPI()


# ---------------------------
# Helper Function
# ---------------------------

def validate_object_id(id: str):
    """Validate and convert a string ID to ObjectId."""
    try:
        return ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")


# ---------------------------
# User Management Endpoints
# ---------------------------

@app.post("/users/register")
async def register_user(user: dict):
    """Register a new user."""
    existing_user = await db["users"].find_one({"email": user["email"]})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    result = await db["users"].insert_one(user)
    return {"id": str(result.inserted_id), "message": "User registered successfully"}


@app.post("/users/login")
async def login_user(credentials: dict):
    """Login a user."""
    user = await db["users"].find_one({"email": credentials["email"]})
    if not user or user["password"] != credentials["password"]:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"message": "Login successful"}


# ---------------------------
# Transaction Management Endpoints
# ---------------------------

@app.post("/transactions")
async def add_transaction(transaction: dict):
    """Add a new financial transaction."""
    result = await db["transactions"].insert_one(transaction)
    return {"id": str(result.inserted_id), "message": "Transaction added successfully"}


@app.get("/transactions/{user_id}")
async def get_transactions(user_id: str):
    """Get all transactions for a user."""
    transactions = await db["transactions"].find({"user_id": user_id}).to_list(100)

    # Convert ObjectId to string for each transaction
    for transaction in transactions:
        transaction["_id"] = str(transaction["_id"])

    return {"transactions": transactions}


@app.put("/transactions/{transaction_id}")
async def update_transaction(transaction_id: str, transaction: dict):
    """Update a financial transaction."""
    object_id = validate_object_id(transaction_id)

    # Find and update transaction
    result = await db["transactions"].update_one({"_id": object_id}, {"$set": transaction})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return {"message": "Transaction updated successfully"}


@app.delete("/transactions/{transaction_id}")
async def delete_transaction(transaction_id: str):
    """Delete a financial transaction."""
    object_id = validate_object_id(transaction_id)

    result = await db["transactions"].delete_one({"_id": object_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return {"message": "Transaction deleted successfully"}


# ---------------------------
# Category Management Endpoints
# ---------------------------

@app.post("/categories")
async def add_category(category: dict):
    """Add a custom category for transactions."""
    result = await db["categories"].insert_one(category)
    return {"id": str(result.inserted_id), "message": "Category added successfully"}


@app.get("/categories")
async def get_categories(user_id: str):
    """Get all categories for a specific user."""
    # Fetch categories for the given user ID
    categories = await db["categories"].find({"user_id": user_id}).to_list(100)
    
    # Convert ObjectId to string for each category
    for category in categories:
        category["_id"] = str(category["_id"])
    
    return {"categories": categories}



@app.put("/categories/{category_id}")
async def update_category(category_id: str, category: dict):
    """Update a category."""
    object_id = validate_object_id(category_id)

    result = await db["categories"].update_one({"_id": object_id}, {"$set": category})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Category not found")

    return {"message": "Category updated successfully"}


@app.delete("/categories/{category_id}")
async def delete_category(category_id: str):
    """Delete a category."""
    object_id = validate_object_id(category_id)

    result = await db["categories"].delete_one({"_id": object_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Category not found")

    return {"message": "Category deleted successfully"}


# ---------------------------
# Savings Goals Endpoints
# ---------------------------

@app.post("/savings-goals")
async def add_savings_goal(goal: dict):
    """Set a savings goal."""
    result = await db["savings_goals"].insert_one(goal)
    return {"id": str(result.inserted_id), "message": "Savings goal added successfully"}


@app.get("/savings-goals/{user_id}")
async def get_savings_goals(user_id: str):
    """Get all savings goals for a user."""
    goals = await db["savings_goals"].find({"user_id": user_id}).to_list(100)

    # Convert ObjectId to string for each savings goal
    for goal in goals:
        goal["_id"] = str(goal["_id"])

    return {"goals": goals}


@app.put("/savings-goals/{goal_id}")
async def update_savings_goal(goal_id: str, goal: dict):
    """Update a savings goal."""
    object_id = validate_object_id(goal_id)

    result = await db["savings_goals"].update_one({"_id": object_id}, {"$set": goal})
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Savings goal not found")

    return {"message": "Savings goal updated successfully"}


@app.delete("/savings-goals/{goal_id}")
async def delete_savings_goal(goal_id: str):
    """Delete a savings goal."""
    object_id = validate_object_id(goal_id)

    result = await db["savings_goals"].delete_one({"_id": object_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Savings goal not found")

    return {"message": "Savings goal deleted successfully"}


# ---------------------------
# Reports Endpoints
# ---------------------------

@app.get("/reports/{user_id}/monthly")
async def generate_monthly_report(user_id: str):
    """Generate monthly report for income, expenses, and savings."""
    
    # Fetch all transactions for the given user ID
    transactions = await db["transactions"].find({"user_id": user_id}).to_list(100)
    
    # Convert ObjectId to string for each transaction
    for transaction in transactions:
        transaction["_id"] = str(transaction["_id"])
    
    # Calculate totals
    total_income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    total_expenses = sum(-t["amount"] for t in transactions if t["amount"] < 0)
    net_savings = total_income - total_expenses

    # Filter transactions for the current month
    from datetime import datetime
    current_month = datetime.now().month
    current_year = datetime.now().year
    monthly_transactions = [
        t for t in transactions if datetime.strptime(t["transaction_date"], "%Y-%m-%d").month == current_month and datetime.strptime(t["transaction_date"], "%Y-%m-%d").year == current_year
    ]

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_savings": net_savings,
        "monthly_transactions": monthly_transactions,
        "message": "Monthly report generated successfully"
    }
