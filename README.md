# Flask Todo REST API

A simple REST API built using **Flask** that supports CRUD operations for managing todo items.

## Features

* Get all items
* Get item by ID
* Create a new item
* Update an item
* Delete an item
* Mark tasks as completed
* Health check endpoint

## Technologies Used

* Python
* Flask
* REST API
* Postman (for testing)

## Item Structure

Each item in the API follows this format:

{
"id": 1,
"name": "Learn Flask",
"completed": false
}

## API Endpoints

GET /items
GET /items/<id>
POST /items
PUT /items/<id>
DELETE /items/<id>
GET /health

## Example POST Request

POST /items

{
"name": "Finish Flask Project"
}

## Run the Project

Install dependencies:

pip install -r requirements.txt

Run the server:

python app.py

Then open:

http://127.0.0.1:5000/items

## Author

Manaswa Medhi
