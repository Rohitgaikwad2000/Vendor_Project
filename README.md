# Vendor Management System

# Overview:-
    The Vendor Management System is an API built using Django and Django REST Framework. It provides endpoints for managing vendors, purchases, and performance metrics.

# Installation

1. Clone the repository:-
git clone <repository-url>

2. Navigate to the project directory:-
cd Vender_System

3. Install dependencies:-
pip install -r requirements.txt

4. Set up the database in settings.py file:-

Add Your database details:-
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'Vender_System',
        'USER': 'Add Your User Here',
        'PASSWORD': 'Add Your Password Here',
        'HOST': 'Add Your host Here',
        'PORT': Add Your Port Here,
    }
}

Then run migrate:-  python manage.py migrate


5. Use this command for Create a superuser for admin page:-

python manage.py createsuperuser



# Running the Development Server:-

Start the development server by running:-
python manage.py runserver

The server will start running at http://localhost:8000/.

Admin page: http://127.0.0.1:8000/admin/


# Token Generation:- 
This API is secured by token-based authentication. To access it:
    1. Generate a token in the admin page by logging in.
    2. Include the token in the request header when making requests to the API. Use the Authorization header prefixed with the string "Token".
    Example: headers = {'Authorization': 'Token your_token_here'} in Postman or Thunder Client.


# API Endpoints:- 
Use token to access APIs.

# Vendors:-
`GET /api/vendors/`: List all vendors
`POST /api/vendors/`: Create a new vendor
`GET /api/vendors/<int:id>/`: Retrieve a specific vendor
`PUT /api/vendors/<int:id>/`: Update a specific vendor
`DELETE /api/vendors/<int:id>/`: Delete a specific vendor


# Purchase:- 
`GET /api/Purchase/`: List all purchase orders
`POST /api/Purchase/`: Create a new purchase order
`GET /api/Purchase/<int:id>/`: Retrieve a specific purchase order
`PUT /api/Purchase/<int:id>/`: Update a specific purchase order
`DELETE /api/Purchase/<int:id>/`: Delete a specific purchase order
`POST /api/purchase_orders/<int:pk>/acknowledge/`: Acknowledge a purchase order


# Historic Metrics:-

`GET /api/Historical/`: List all performance metrics
`POST /api/Historical/`: Create a new performance metric
`GET /api/Historical/<int:pk>/`: Retrieve a specific performance metric
`PUT /api/Historical/<int:pk>/`: Update a specific performance metric
`DELETE /api/Historical/<int:pk>/`: Delete a specific performance metric
`GET /api/vendors/<int:pk>/performance/`: Retrieve performance metrics for a specific vendor


# Running the Test Suite:- 

Execute the following command in your terminal for test suite run:- 
python manage.py test

All the tests defined in the tests.py file and display the results.