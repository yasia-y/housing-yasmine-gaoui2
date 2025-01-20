Flask and PostgreSQL Integration with Python
Overview

This project demonstrates how to integrate a Python Flask web application with a PostgreSQL database. It includes tools for database migrations and creation using Flask-Migrate and psycopg2.
Prerequisites
Tools and Libraries

    Python
    PostgreSQL
    Flask
    Flask-Migrate
    psycopg2

Setup

Before running the application, ensure you have the following:

    Python virtual environment (venv) activated.
    PostgreSQL server running.

Installation
Step 1: Clone the Repository

git clone https://github.com/kilianMeddas/housing-Kilian-Meddas.git
cd housing-Kilian-Meddas
cd housing_api

Step 2: Set Up Virtual Environment

python -m venv venv (optional)
source venv/bin/activate  # On Windows: venv\Scripts\activate

Step 3: Install Dependencies (optional)

pip install -r requirements.txt

Step 4: Configure PostgreSQL

Update the PostgreSQL credentials in the create_db.py and app_migration.py files:

conn = psycopg.connect(database="postgres", user="postgres", password="your_password", host="127.0.0.1", port="5432")

Ensure the postgres database exists, and the user has the necessary permissions to create additional databases and tables.
Running the Application
Step 1: Create the Database

Run the create_db.py script to set up the house database:

python create_db.py

Step 2: Initialize and Apply Migrations
Initialize Migrations

Run the following commands to initialize Flask-Migrate:

export FLASK_APP=app_migration.py
flask db init

Generate Migration Script

Create a migration script based on your models:

flask db migrate -m "Initial migration."

Apply Migrations

Apply the migration script to the database:

flask db upgrade

Run app

Apply the migration script to the database:

python app_migration.py

API Endpoints
GET /houses

Retrieve all house entries from the houses table.
Response Example

[
  {
    "house_id": 1,
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "median_house_value": 452600,
    "ocean_proximity": "NEAR BAY"
  }
]

POST /houses

Add a new house entry to the houses table.
Request Body Example

{
  "house_id": 2,
  "longitude": -122.22,
  "latitude": 37.86,
  "housing_median_age": 21,
  "total_rooms": 7099,
  "total_bedrooms": 1106,
  "population": 2401,
  "households": 1138,
  "median_income": 8.3014,
  "median_house_value": 358500,
  "ocean_proximity": "NEAR BAY"
}

Response

{
  "message": "House added successfully!"
}

Notes

    The application automatically checks for the existence of the houses table and the house database. If not found, they are created at runtime.
    Errors during runtime are logged to the console. Enable Flask's debug mode for detailed logs.

Troubleshooting
Common Issues

    Connection Error: Ensure PostgreSQL is running and credentials are correct.
    Module Not Found: Run pip install -r requirements.txt to install dependencies.

Logs

All logs are printed to the console. Use debug=True in the app.run() method to see detailed error messages during development.
License

This project is licensed under the MIT License.
