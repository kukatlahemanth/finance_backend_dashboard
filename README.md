Finance Dashboard Backend API

 Overview

This project is a backend system for a finance dashboard that manages financial transactions and enforces role-based access control.
It allows different types of users (Admin, Analyst, Viewer) to interact with financial data based on their permissions and provides summary analytics for decision-making.

Key Features

JWT Authentication (Secure login system)
Role-Based Access Control (RBAC)
Financial Records Management (CRUD APIs)
Filtering (by type and category) 
Dashboard Analytics (income, expenses, balance)
Validation and Error Handling


Tech Stack

| Technology            | Purpose          |
| --------------------- | ---------------- |
| Python                | Backend language |
| Django                | Web framework    |
| Django REST Framework | API development  |
| SimpleJWT             | Authentication   |
| SQLite                | Database         |
| Postman               | API Testing      |


Project Structure

```
finance_backend/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── finance_dashboard/        # Main Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/                     # Main app (handles all logic)
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── models.py             # User & Financial models
│   ├── serializers.py        # DRF serializers
│   ├── views.py              # API views
│   ├── permissions.py        # Role-based access control
│   ├── urls.py               # App routes
│   ├── admin.py
│   ├── apps.py
│   └── tests.py
│
├── db.sqlite3                # Database
│
└── .env                      # Environment variables (optional)
---

Setup Instructions

Clone Repository

```bash
git clone <your_repo_link>
cd finance_dashboard
```
Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

Install Dependencies

```bash
pip install -r requirements.txt
```
Note: Dependencies include Django, Django REST Framework, SimpleJWT, and any other packages required.

Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create Superuser

```bash
python manage.py createsuperuser
```

Run Server

```bash
python manage.py runserver
```

---

Authentication

Get JWT Token

```http
POST /api/token/
```

Request:

```json
{
  "username": "admin",
  "password": "your_password"
}
```

Response:

```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

---

API Endpoints

Financial Records

| Method | Endpoint           | Access    | Description      |
| ------ | ------------------ | --------- | ---------------- |
| GET    | /api/records/      | All roles | Retrieve records |
| POST   | /api/records/      | Admin     | Create record    |
| PUT    | /api/records/{id}/ | Admin     | Update record    |
| DELETE | /api/records/{id}/ | Admin     | Delete record    |

---

Filtering

```http
GET /api/records/?type=income
GET /api/records/?category=salary
GET /api/records/?date=2026-04-06

```

---

Dashboard Summary

```http
GET /api/dashboard/
```

Example Response:

```json
{
  "total_income": 5000,
  "total_expense": 200,
  "net_balance": 4800
}
```

---

Role-Based Access Control

| Role    | Permissions      |
| --------| ---------------- |
| Viewer  | Dashboard        |
| Analyst | Read + dashboard |
| Admin   | Full CRUD access |

---

Business Logic

* Income and expense are stored as separate record types
* Aggregation is performed using Django ORM (`Sum`)
* Net balance is calculated as:

```
Net Balance = Total Income - Total Expense
```

---

 Error Handling

| Status Code | Meaning                              |
| ----------- | ------------------------------------ |
| 400         | Invalid input                        |
| 401         | Unauthorized (missing/invalid token) |
| 403         | Forbidden (role restriction)         |
| 404         | Resource not found                   |

---

Future Enhancements

* Pagination for large datasets
* Search functionality
* Category-wise analytics
* Monthly/weekly reports
* API documentation (Swagger)

---

Author

**Hemanth**
Backend Developer Intern Candidate

---

Notes

This project is designed to demonstrate backend architecture, API design, access control, and data processing skills in a clean and maintainable way.
