# 🛒 Django eCommerce API

A full-featured, production-ready **eCommerce API backend** built with **Django**, **DRF**, **Docker**, and **PostgreSQL** — inspired by real-world platforms like Flipkart and Amazon.

---

## 🚀 Features

- ✅ Custom User Model with Email Login
- 🔐 JWT Authentication (SimpleJWT)
- 🛍️ Product Catalog with Categories & Brands
- 🛒 Cart & Wishlist Management
- 🧾 Order Placement and Tracking
- 💳 Payment Integration (Stripe / Razorpay)
- 📨 Email & SMS Notifications
- ⚙️ Dockerized Backend
- ⏱️ Async Tasks with Celery + Redis
- ☁️ Deployment with Nginx + Gunicorn + GitHub CI/CD

---

## 📁 Project Structure
shopapi/
├── accounts/ # Auth: Custom user + JWT
├── products/ # Product catalog (coming)
├── orders/ # Orders & payments (coming)
├── config/ # Django settings and URLs
├── manage.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile # For full app Dockerization
└── .env # Environment config


---

## 🐳 Getting Started (Docker)

### 1️⃣ Clone the repo & enter the project folder

```bash
git clone https://github.com/your-username/shopapi.git
cd shopapi

# .env
DB_NAME=shopdb
DB_USER=shopuser
DB_PASSWORD=shoppass
DB_HOST=db
DB_PORT=5432

docker compose up -d
python -m venv shopenv
source shopenv/bin/activate  # or shopenv\Scripts\activate on Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


