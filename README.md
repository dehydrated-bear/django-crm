# 🧾 RESTful Inventory Management System (Product Management API)

A fully functional RESTful Inventory Management System built using **Django REST Framework**, offering secure product management, JWT-based authentication, Algolia-powered search, and a simple JavaScript-based client frontend.

---

## 🚀 Features

✅ Full CRUD (Create, Read, Update, Delete) operations for managing products  
✅ **JWT Authentication** for secure login and protected endpoints  
✅ **Algolia integration** for lightning-fast and scalable product search  
✅ Modular backend structure for better scalability and maintainability  
✅ JavaScript-based client to interact with API endpoints  
✅ Custom session management and request handling to track user interactions  

---

## 🛠️ Tech Stack

- **Backend**: Django • Django REST Framework  
- **Authentication**: JWT (JSON Web Token)  
- **Search Engine**: [Algolia](https://www.algolia.com/)  
- **Frontend**: Vanilla JavaScript (Client App)  
- **Others**: Django Sessions, Custom Middleware

---

## 🧪 Running Locally

### 1. Clone the repo:

git clone https://github.com/yourusername/inventory-management-api.git
cd inventory-management-api

###2. Create a virtual environment & install dependencies:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

3. Setup Algolia keys:
Create a .env file and add:

ALGOLIA_APP_ID=your_app_id
ALGOLIA_API_KEY=your_admin_key
ALGOLIA_INDEX_NAME=products
4. Run the server
python manage.py runserver


