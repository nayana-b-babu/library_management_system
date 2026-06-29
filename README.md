# Library Management System

A Django-based library management system for managing books, issuing, returning, and purchasing records.

## Features
- User signup and login
- Book management
- Issue and return workflows
- Purchase records

## Setup
1. Create and activate a virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Notes
- The project uses SQLite by default.
- Static files and uploaded media are stored in the local project folders.
