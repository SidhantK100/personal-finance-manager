#### Add a Transaction 


Endpoint: POST /transactions

Purpose: To add a financial transaction for the user.

Steps:

Click on POST /transactions in Swagger UI.

Click Try it out.

Enter the following JSON body:

{
  "user_id": "<user_id>",
  "amount": 500,
  "transaction_date": "2025-03-07",
  "category": "Food",
  "description": "Grocery shopping"
}
Replace <user_id> with the id you copied from Step 1. 

Click Execute.

Copy the id from the response (e.g., "id": "67cb2e2b75b7f685836826d4"). This is the transaction_id needed for subsequent steps. 


##### Retrieve Transactions for a User 

Endpoint: GET /transactions/{user_id}

Purpose: To retrieve all transactions for a specific user.

Steps:

Click on GET /transactions/{user_id} in Swagger UI.

Click Try it out.

Enter <user_id> in the path parameter (copied from Step 1).

Click Execute.

Verify that all transactions for this user are listed in the response. 


#### Update a Transaction


Endpoint: PUT /transactions/{transaction_id}

Purpose: To update an existing transaction.

Steps:

Click on PUT /transactions/{transaction_id} in Swagger UI.

Click Try it out.

Enter <transaction_id> in the path parameter (copied from Step 3).

Enter the following JSON body:

{
  "amount": 200,
  "category": "Dining",
  "description": "Dinner expense"
}

Click Execute.

Verify that the response says "message": "Transaction updated successfully".

