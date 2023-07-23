# DjanShop

[![Python Version](https://img.shields.io/badge/Python-3.11.4-blue.svg)](https://www.python.org/downloads/release/python-3114/)
[![Django Version](https://img.shields.io/badge/Django-3.2+-green.svg)](https://www.djangoproject.com/)
[![Django Rest Framework Version](https://img.shields.io/badge/Django%20Rest%20Framework-3.12+-red.svg)](https://www.django-rest-framework.org/)

## Description
A Django-React ecommerce app backend

## Requirements

- Python 3.11+
- Django 3.2+
- Django Rest Framework 3.12+
- Pipenv

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ZhitingLu/DjanShop.git
```

2. Change into the project directory:

```bash
cd DjanShop
```

3. Install dependencies using Pipenv:

```bash
pipenv install --dev
```

-- If you need to install pipenv:
  ```bash
pip install --user pipenv
  ```

4. Activate the virtual environment:

```bash
pipenv shell
```

5. Run database migrations:

```bash
python manage.py migrate
```

6. Create a superuser (if needed):

```bash
python manage.py createsuperuser
```

## Usage

```bash
python manage.py runserver
```
