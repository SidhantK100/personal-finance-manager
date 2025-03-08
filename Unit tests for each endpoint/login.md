2.Login with the Registered User
Endpoint: POST /users/login

Purpose: To authenticate the user.

Steps:

Click on POST /users/login in Swagger UI.

Click Try it out.

Enter the following JSON body: 

{
  "email": "john.doe@example.com",
  "password": "password123"
}
Click Execute.

Ensure the response says "message": "Login successful". 