1. Register a New User
Endpoint: POST /users/register

Purpose: To create a new user.

Steps:

Click on POST /users/register in Swagger UI.

Click Try it out.

Enter the following JSON body: 

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "password123"
}
 
Click Execute.

Copy the id from the response (e.g., "id": "67cb2e2b75b7f685836826d4"). This is the user_id needed for subsequent steps.