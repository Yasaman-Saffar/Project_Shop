# Simple Django E-commerce Project

A beginner-friendly e-commerce web application built with Django, designed to showcase basic backend and form-handling concepts.

---

## Features

- Add new products through a public form (no login required)
- Upload product images
- Display all products on the homepage
- View each product in a separate detail page
- Submit support tickets via a contact form
- Basic admin panel to manage products and tickets
- Frontend styled using Bootstrap 5

---

## Technologies Used

- Python 3.11.7
- Django 5.2.4
- Bootstrap 5
- PostgreSQL
- HTML & CSS
- Pillow (for image handling)

---

## Screenshots

### Homepage
![Homepage](screenshots/Homepage.png)

### Add Product Form
![Add Product](screenshots/Add-product-form.png)

### Product Detail Page
![Product Detail](screenshots/product-detail.png)

### Add Ticket Page
![Add Ticket](screenshots/Ticket-form.png)

---

## How to Run This Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/Yasaman-Saffar/Project_Shop.git
   cd Project_Shop
   ```
   
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   # On Windows: venv\Scripts\activate
   # On macOs/Linux: source venv/bin/activate
   ```
   
3. Install project dependencies
  ```bash
  pip install -r requirements.txt
  ```

4. Set up environment variables
  Create a .env file in the root of your project (next to manage.py) and add the following variables:
  ```bash
  DB_NAME=your_postgres_database
  DB_USER=your_database_user
  DB_PASSWORD=your_database_password
  DB_HOST=localhost
  DB_PORT=5432
  ```

5. Apply database migrations
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

6. Create a superuser (optional)
  ```bash
  python manage.py createsuperuser
  ```

7. Start the development server
  ```bash
  python manage.py runserver
  ```

9. Access the application in your browser
  ```bash
  http://127.0.0.1:8000/
  ```
