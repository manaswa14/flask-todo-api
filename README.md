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

## Example Item

{
  "id": 1,
  "name": "Learn Flask",
  "completed": false
}
## API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | /items | Get all items |
| GET | /items/<id> | Get item by id |
| POST | /items | Create item |
| PUT | /items/<id> | Update item |
| DELETE | /items/<id> | Delete item |
| GET | /health | Check API status |



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
