E-Commerce Order Management System

Overview

The E-Commerce Order Management System is a FastAPI-based backend application that manages customers, products, orders, and shipments. The system includes JWT Authentication, Role-Based Authorization, Product Inventory Management, Order Processing, Shipment Tracking, Filtering, Pagination, Background Tasks, and Database Integration using SQLAlchemy.

Features

Authentication & Authorization

* User Registration
* User Login
* JWT Authentication
* Role-Based Access Control (Admin / Customer)

Customer Management

* Create Customer
* Get All Customers
* Get Customer by ID
* View Customer Orders

Product Management

* Create Product
* Update Product
* Deactivate Product
* Filter Products by Category
* Pagination Support
* Prevent Ordering Inactive Products

Order Management

* Create Orders
* Multiple Order Items
* Auto Calculate Total Amount
* Stock Validation
* Reduce Stock After Order
* Prevent Negative Stock
* Filter Orders by Status
* Pagination Support

Shipment Management

* Create Shipment
* Update Shipment Status
* Get Shipment Details
* Filter Shipments by Status
* One Shipment Per Order
* Unique Tracking Number Validation
* Pagination Support

Additional Features

* SQLAlchemy ORM
* SQLite Database
* Background Tasks
* CORS Middleware
* Environment Configuration
* Docker Support
* Pytest Testing



Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* JWT Authentication
* Python
* Pytest
* Docker



Project Structure

ecommerce_order_management/

app/

* models/
* schemas/
* routes/
* services/
* utils/
* core/

tests/

main.py
database.py
requirements.txt
Dockerfile
README.md



Installation

Clone Repository

git clone <repository-url>

cd ecommerce_order_management

Create Virtual Environment

python -m venv venv

Activate Virtual Environment

Windows:

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt



Run Application

uvicorn app.main:app --reload

Application URL:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs



API Endpoints

 Authentication

POST /api/v1/auth/register

POST /api/v1/auth/login

Customers

GET /api/v1/customers/

POST /api/v1/customers/

GET /api/v1/customers/{id}

Products

GET /api/v1/products/

POST /api/v1/products/

PUT /api/v1/products/{id}

DELETE /api/v1/products/{id}

GET /api/v1/products/filter/

Orders

GET /api/v1/orders/

POST /api/v1/orders/

GET /api/v1/orders/{id}

Shipments

POST /api/v1/shipments/

PUT /api/v1/shipments/{id}

GET /api/v1/shipments/{id}

GET /api/v1/shipments/



Business Rules

* Customer can place multiple orders.
* Inactive products cannot be ordered.
* Product stock is validated before order creation.
* Stock is automatically reduced after successful order.
* Stock cannot become negative.
* One shipment per order.
* Tracking number must be unique.
* Delivered orders cannot be cancelled.
* Quantity must be greater than zero.
* Price must be greater than zero.
* Customer email must be unique.



Testing

Run Tests:

pytest

Current Status:

All tests passing successfully.



 Docker

Build Docker Image:

docker build -t ecommerce-app .

Run Docker Container:

docker run -p 8000:8000 ecommerce-app



Order Flow

1. Register User
2. Login User
3. Create Customer
4. Create Product
5. Create Order
6. Validate Product Stock
7. Reduce Product Stock
8. Create Shipment
9. Update Shipment Status
10. Deliver Shipment



Author

Tharun

FastAPI Enhancement Assignment – E-Commerce Order Management System
