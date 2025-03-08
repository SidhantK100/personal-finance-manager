#### Add a Savings Goal


Endpoint: POST /savings-goals

Purpose: To set a savings goal for a user.

Steps:

Go to Swagger UI (http://127.0.0.1:8000/docs).

Click on POST /savings-goals.

Click Try it out.

Enter the following JSON body:

{
  "user_id": "<user_id>",
  "target_amount": 10000,
  "target_date": "2025-12-31"
}
Replace <user_id> with the actual user ID from the POST /users/register endpoint.

Click Execute.

Copy the id from the response (e.g., "id": "def456uvw"). This is the goal_id needed for subsequent steps.

Expected Response:

{
  "id": "<generated_savings_goal_id>",
  "message": "Savings goal added successfully"
}


#### Retrieve Savings Goals for a User 


Endpoint: GET /savings-goals/{user_id}

Purpose: To retrieve all savings goals for a specific user.

Steps:

Go to Swagger UI (http://127.0.0.1:8000/docs).

Click on GET /savings-goals/{user_id}.

Click Try it out.

Enter the user_id from the response of the POST /users/register endpoint (e.g., "67cb2e2b75b7f685836826d4") in the path parameter.

Click Execute.

Verify that all savings goals for this user are listed in the response.

Expected Response:

{
  "goals": [
    {
      "_id": "def456uvw",
      "user_id": "<user_id>",
      "target_amount": 10000,
      "target_date": "2025-12-31"
    }
  ]
} 



#### Update a Savings Goal 

Endpoint: PUT /savings-goals/{goal_id}

Purpose: To update an existing savings goal.

Steps:

Go to Swagger UI (http://127.0.0.1:8000/docs).

Click on PUT /savings-goals/{goal_id}.

Click Try it out.

Enter the goal_id from the response of the POST /savings-goals endpoint (e.g., "def456uvw") in the path parameter.

Enter the following JSON body:

{
  "target_amount": 12000,
  "target_date": "2025-11-30"
} 

Click Execute.

Expected Response:

{
  "message": "Savings goal updated successfully"
}



#### Delete a Savings Goal


Endpoint: DELETE /savings-goals/{goal_id}

Purpose: To delete an existing savings goal.

Steps:

Go to Swagger UI (http://127.0.0.1:8000/docs).

Click on DELETE /savings-goals/{goal_id}.

Click Try it out.

Enter the goal_id from the response of the POST /savings-goals endpoint (e.g., "def456uvw") in the path parameter.

Click Execute.

Expected Response:

{
  "message": "Savings goal deleted successfully"
} 
