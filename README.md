# HardQodeTest

This project is a solution to the test task "Building a system for training." It was created to test knowledge of building relationships in the database and the ability to correctly build queries without N+1 errors.

## Description

The challenge is to create a learning system using Django and SQLite. The system includes models of products, lessons, user groups and mechanisms for distributing users into groups depending on access to products. It is also necessary to implement a REST API for working with products and lessons, as well as for displaying statistics on products.

## Installation and use

### Clone the repository:

```bash
git clone https://github.com/yourusername/yourproject.git
```

### Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate # For Linux/Mac
venv\Scripts\activate # For Windows
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Apply migrations:

```bash
python manage.py migrate
```

### Start the development server:

```bash
python manage.py runserver
```

### Testing
To run the tests, run the following command:

```bash
python manage.py test
```
