# Personal Finance Manager

## Overview
This is a backend application for managing personal finances, built using FastAPI and MongoDB. The system allows users to:
- Register and log in.
- Add, view, update, and delete financial transactions.
- Manage custom categories for transactions.
- Set and track savings goals.
- Generate monthly reports for income, expenses, and savings.

## Features
- **User Management**: Register and log in users with unique profiles.
- **Transaction Management**: Add, view, update, and delete transactions categorized by type (e.g., Food, Rent).
- **Category Management**: Add custom categories for transactions and manage them.
- **Savings Goals**: Set savings goals with target amounts and dates.
- **Reports**: Generate monthly reports showing spending patterns.

## Setup Instructions

### Prerequisites
- Python 3.9 or higher installed on your system.
- MongoDB Atlas account for database hosting.
  - Whitelist your current ip under network-access
  - Copy your URI under database access

### Installation Steps
1. Clone this repository:
git clone https://github.com/SidhantK100/personal-finance-manager.git
cd personal-finance-manager 

2. Install dependencies:
pip install -r requirements.txt 

3. Create a `.env` file in the root directory with the following content:
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/personal_finance_manager?retryWrites=true&w=majority 

Replace `<username>` and `<password>` with your MongoDB Atlas credentials.

4. Run the application:

uvicorn app.main:app --reload 

5. Access Swagger UI at `http://127.0.0.1:8000/docs`.

## Assumptions Made

- Basic authentication is implemented using email and password.
- MongoDB Atlas is used as the database. 

## for testing purpose access the unit test folder from the root directory .