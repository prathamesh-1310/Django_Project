Library Management System (LMS)

This is a Django-based Library Management System that helps to manage books, authors, and users efficiently.

Features:
- Home Page: Displays all available books.
- Book Management: Add, edit, delete books.
- Search Books: Search by title, author, or ISBN.
- Admin Panel: Manage books and users via Django admin.
- API Support: Fetch book details via Django REST Framework.

Required Packages & Dependencies:
- Django: Web framework (`pip install django`)
- Django REST Framework (DRF): API toolkit (`pip install djangorestframework`)
- Pillow: Image handling (`pip install pillow`)
- psycopg2: PostgreSQL adapter (`pip install psycopg2`)
- mysqlclient: MySQL adapter (`pip install mysqlclient`)
- django-cors-headers: Handles CORS (`pip install django-cors-headers`)

To generate `requirements.txt`:
```
pip freeze > requirements.txt
```

To install all dependencies:
```
pip install -r requirements.txt
```

How to Run the Project:
1. Clone the repository:
```
git clone https://github.com/prathamesh-1310/Django_Project.git
cd Django_Project
```

2. Create a virtual environment:
```
python -m venv venv
```
- On Windows: `venv\Scripts\activate`
- On Mac/Linux: `source venv/bin/activate`

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Set up the database:
- Open `settings.py` and update the `DATABASES` section with your database credentials.

5. Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```

6. Create an admin user:
```
python manage.py createsuperuser
```
- Enter a username, email, and password.

7. Run the server:
```
python manage.py runserver
```

API Endpoints:
- `GET /api/books/` - Get all books
- `POST /api/books/` - Add a new book
- `PUT /api/books/<id>/` - Update a book
- `DELETE /api/books/<id>/` - Delete a book

Accessing Admin Panel:
- URL: `http://127.0.0.1:8000/admin/`
- Login with the superuser credentials created in step 6.

Notes:
- Ensure the database is correctly configured in `settings.py`.
- If using MySQL, start MySQL Server before running Django.
- Use Postman or cURL to test API endpoints.





