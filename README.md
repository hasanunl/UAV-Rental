# UAV Rental Project with Django

## Overview

This web application let's users rent UAVs for their needs.

Features that have currently been implemented are:

* Membership and Login Screen
* For the UAV to be rented; Add, Delete, Update, List, Rent
* Members' UAV rental records
* Unit testing
* Documentation 
* Front-End Bootstrap usage
* Keeping relational tables separately

## Entity Relationships
* Brand (brand_name) - Defines the brands that manufacture UAVs.
* Category (type) - Defines the categories for UAV types.
* Uav (model, brand (fk) , weight, category) - Defines a UAV model. Has to have a Brand. Can have multiple categories.
* UavInstace (id, uav (fk) , renter (fk) , return_date) - Defines the rentable UAVs based on the existing UAV model.

## How to start the application
To get the UAV Rental project up and running locally on your computer:
1. Set up the Python development environment
1. Run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type. You have to create the UAV models here as you can only create UAV instances from existing models in home page.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.