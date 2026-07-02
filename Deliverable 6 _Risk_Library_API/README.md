# Risk Library API

## Project Overview

The Risk Library API is a RESTful backend application developed using FastAPI and MongoDB. It provides a centralized repository for managing AI-related risks associated with Retrieval-Augmented Generation (RAG) and Agentic AI systems. The API supports complete CRUD operations, risk searching, and data validation using Pydantic models.

---

## Technologies Used

- FastAPI
- MongoDB
- PyMongo
- Pydantic
- Uvicorn
- Python

---

## Folder Structure

```
FastAPI_MongoDB
│
├── main.py
├── models.py
├── database.py
├── crud.py
├── seed_data.py
├── requirements.txt
└── README.md
```

---

## Risk Fields

Each risk contains the following fields:

- id
- name
- description
- category
- severity
- archetype
- trust_attribute
- created_at
- version

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------------|------------------------------|
| GET | / | Home |
| GET | /about | Project Information |
| POST | /risks | Create New Risk |
| GET | /risks | Get All Risks |
| GET | /risks/{id} | Get Risk by ID |
| PUT | /risks/{id} | Update Risk |
| DELETE | /risks/{id} | Delete Risk |
| GET | /search | Search by Archetype and Severity |

---

## Search Example

GET

```
/search?archetype=RAG&severity=high
```

---

## Running the Project

Install dependencies

```bash
py -m pip install -r requirements.txt
```

Run FastAPI

```bash
py -m uvicorn main:app --reload
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

---

## Seed Sample Data

Run

```bash
py seed_data.py
```

This inserts:

- 3 RAG Risks
- 3 Agentic Risks

---

## MongoDB

Database

```
risk_library_db
```

Collection

```
risk_library
```

---

## Project Features

- FastAPI REST API
- MongoDB Integration
- Pydantic Validation
- CRUD Operations
- Search by Archetype
- Search by Severity
- MongoDB Indexing
- Sample Seed Data
- Swagger Documentation

---

## Author

Medikonda Hemanth Rishi