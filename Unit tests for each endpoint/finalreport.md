#### Generate Monthly Report 


Endpoint: GET /reports/{user_id}/monthly

Purpose: To generate a monthly report for income, expenses, and savings.

Steps:

Go to Swagger UI (http://127.0.0.1:8000/docs).

Click on GET /reports/{user_id}/monthly.

Click Try it out.

Enter the user_id from the response of the POST /users/register endpoint (e.g., "67cb2e2b75b7f685836826d4") in the path parameter.

Click Execute.

Verify that the response includes total income, expenses, net savings, and a list of transactions for the month.

Expected Response:

{
  "total_income": 500,
  "total_expenses": 200,
  "net_savings": 300,
  "monthly_transactions": [
    {
      "_id": "67cb2e2b75b7f685836826d4",
      "user_id": "<user_id>",
      "amount": 500,
      "transaction_date": "2025-03-07",
      "category": "Food",
      "description": "Grocery shopping"
    }
  ],
  "message": "Monthly report generated successfully"
}

Make sure do not use delete for the transaction,category and the saving_goals endpoints so that the generate report shows up perfectly