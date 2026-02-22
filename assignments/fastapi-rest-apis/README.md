# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice routing, request/response handling, and working with JSON data in Python.

## 📝 Tasks

### 🛠️ Build Core API Endpoints

#### Description
Create a FastAPI application with basic endpoints that return structured JSON responses and support query parameters.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Add a `GET /` endpoint that returns a welcome message.
- Add a `GET /items` endpoint that returns a list of items.
- Add support for an optional query parameter (for example, `limit`) on `GET /items`.
- Return valid JSON responses for all endpoints.


### 🛠️ Add Data Validation and Create Endpoint

#### Description
Add a POST endpoint that accepts new item data, validates it with a Pydantic model, and stores it in memory.

#### Requirements
Completed program should:

- Define an `Item` model with at least `name` and `price` fields.
- Add a `POST /items` endpoint that accepts an `Item` payload.
- Validate request data using the Pydantic model.
- Save created items in an in-memory list.
- Return the created item and display clear success behavior when tested.
