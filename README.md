# 📇 Django CRM — Lightweight Customer Relationship Management System

A lightweight, extensible CRM (Customer Relationship Management) web application built with **Django 5.1.5**, designed to streamline lead and contact management for small teams and individual professionals.

---

## 🚀 Features

✅ Lead and contact tracking via a user-friendly web interface  
✅ **Django-crispy-forms** for responsive and elegant form handling  
✅ Custom admin dashboard for managing pipelines and client data  
✅ Clean, readable SQL with **sqlparse** for maintainable queries  
✅ Built with scalability and modularity in mind for future upgrades  

---

## 🛠️ Tech Stack

- **Backend**: Django 5.1.5  
- **Frontend/UI**: HTML • Bootstrap (via crispy-forms)  
- **Form Handling**: [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)  
- **Database**: SQLite (or PostgreSQL-ready)  
- **SQL Formatting**: [sqlparse](https://github.com/andialbrecht/sqlparse)

---

## 🧪 Getting Started

Follow these steps to set up and run the project locally:

1. **Clone the repository**
git clone https://github.com/dehydrated-bear/django-crm.git
cd django-crm

python -m venv venv
# For Linux/macOS:
source venv/bin/activate
# For Windows:
venv\Scripts\activate


pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

