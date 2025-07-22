# `alx_travel_app_0x00` - Database Modeling and Data Seeding

This repository contains the solution for the "Database Modeling and Data Seeding in Django" mandatory task, part of the ALX Backend Web Development curriculum.

## Objective

The primary objective of this task was to define the database models (`Listing`, `Booking`, `Review`), create serializers for API data representation, and implement a Django management command to seed the database with sample data. This lays the foundational data structure for the `alx_travel_app`.

## Project Structure

The core files modified/created for this task are located within the `alx_travel_app` directory:

alx_travel_app_0x00/alx_travel_app/
├── alx_travel_app/
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py           # Updated INSTALLED_APPS, .env setup
│   ├── urls.py
│   └── wsgi.py
├── listings/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── init.py
│   ├── management/             # New directory for custom commands
│   │   └── commands/
│   │       └── seed.py       # Custom command to seed database
│   ├── models.py               # Defines Listing, Booking, Review models
│   ├── serializers.py          # Defines ListingSerializer, BookingSerializer
│   ├── tests.py
│   └── views.py
├── manage.py
├── requirements.txt
└── .env                        # New file for environment variables (e.g., SECRET_KEY)

## Features Implemented

* **Database Models**:
    * `Listing`: Represents a travel accommodation (e.g., apartment, villa, tent) with details such as title, description, location, pricing, capacity, and owner.
    * `Booking`: Manages reservations for a `Listing`, including check-in/out dates, guest information, and total price. Includes a `unique_together` constraint to prevent overlapping bookings.
    * `Review`: Allows guests to provide ratings and comments for a `Listing`.
* **Django REST Framework Serializers**:
    * `ListingSerializer`: Converts `Listing` model instances to JSON format for API responses and handles deserialization for creating/updating listings.
    * `BookingSerializer`: Handles serialization/deserialization for `Booking` instances.
* **Database Seeder**:
    * A custom Django management command (`python manage.py seed`) has been implemented.
    * This command populates the database with sample `User` accounts (hosts and guests), `Listing` entries, `Booking` records, and `Review` data, facilitating easy testing and development.
* **Environment Variables**:
    * Configuration for `SECRET_KEY` is now handled via a `.env` file for better security practices.

## Setup and Installation

Follow these steps to set up the project locally and run the database seeding command.

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* Git

### 1. Clone the Repository

```bash
git clone [https://github.com/ndunguloren96/alx_travel_app_0x00.git](https://github.com/ndunguloren96/alx_travel_app_0x00.git)
cd alx_travel_app_0x00/alx_travel_app
```
2. Create and Activate Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.
```
python3 -m venv .venv
source .venv/bin/activate # On Linux/macOS/WSL2
# .venv\Scripts\activate   # On Windows (Cmd or PowerShell)
```

3. Install Dependencies
Install all required Python packages from the requirements.txt file.
```pip install -r requirements.txt```

4. Configure Environment Variables
Create a .env file in the alx_travel_app directory (the same directory as manage.py) and add your Django SECRET_KEY.

```touch .env```
Open the .env file and add a strong, random SECRET_KEY. You can generate one using Python:

```
import random
import string
chars = ''.join([random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for i in range(50)])
print(chars)
Example .env content:
*SECRET_KEY=your_very_long_and_random_secret_key_generated_above!@#$%^&*
```

5. Run Database Migrations
Apply the database schema changes based on the defined models.
```
python manage.py makemigrations listings
python manage.py migrate
```
6. Seed the Database
Populate the database with sample data using the custom management command.

```python manage.py seed```
You should see output indicating the creation of users, listings, bookings, and reviews.

##Usage
After completing the setup steps, your Django project's database will be populated with sample data. You can now interact with the models via the Django shell, admin interface, or by building out API endpoints using the provided serializers.
