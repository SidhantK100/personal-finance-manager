#### Add a Category

Endpoint: POST /categories

Purpose: To add a custom category for transactions.

Steps:

Provide this JSON body:

{
  "user_id": "<user_id>",
  "name": "Entertainment",
  "description": "Movies, concerts, etc."
} 

Replace <user_id> with the actual user ID from Step 1. 

Click Execute.

Expected Response: 

{
  "id": "<generated_category_id>",
  "message": "Category added successfully"
} 

Copy the id from the response (e.g., "id": "abc123xyz"). This is the category_id needed for subsequent steps.



#### Retrieve Categories for a User 


Endpoint: GET /categories

Purpose: To retrieve all categories for a specific user.

Steps:

Go to Swagger UI (http://127.0.0.1:8000/docs).

Click on GET /categories.

Click Try it out.

Enter the user_id from the response of the POST /users/register endpoint (e.g., "67cb2e2b75b7f685836826d4") in the query parameter.

Click Execute.

Verify that all categories for this user are listed in the response. 

Expected Response:

{
  "categories": [
    {
      "_id": "abc123xyz",
      "user_id": "<user_id>",
      "name": "Entertainment",
      "description": "Movies, concerts, etc."
    }
  ]
}
 

#### Update a Category


Endpoint: PUT /categories/{category_id}

Purpose: To update an existing category.

Steps:

Go to Swagger UI (http://127.0.0.1:8000/docs).

Click on PUT /categories/{category_id}.

Click Try it out.

Enter the category_id from the response of the POST /categories endpoint (e.g., "abc123xyz") in the path parameter.

Enter the following JSON body: 

{
  "name": "Leisure",
  "description": "Relaxation and hobbies"
}

Click Execute.

Expected Response:

{
  "message": "Category updated successfully"
}



#### Delete a Category
Endpoint: DELETE /categories/{category_id}

Purpose: To delete an existing category.

Steps:

Go to Swagger UI (http://127.0.0.1:8000/docs).

Click on DELETE /categories/{category_id}.

Click Try it out.

Enter the category_id from the response of the POST /categories endpoint (e.g., "abc123xyz") in the path parameter.

Click Execute.

Expected Response:

{
  "message": "Category deleted successfully"
} 

