# EconPlaza backend (Django)

[![python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-392/) 
[![django 3.2.8](https://img.shields.io/badge/django-3.2-blue.svg)](https://pypi.org/project/Django/3.2.8/)

## Getting started

Set up and activate a virtual environment:

```bash
$ python -m venv '.env'

$ source .env/bin/activate          # Linux
$ source .env/Scripts/activate      # Windows
```

Install the required packages to your environment.:

```bash
$ pip install -r requirements.txt
```

Navigate to the project directory, where `manage.py` is located.

```bash
$ cd backend
```

Set up your local database by running migrations:

```bash
$ python manage.py migrate
```

Finally, run the server:

```bash
$ python manage.py runserver
```

You can visit it at `http://localhost:8000/` (`http://127.0.0.1:8000/`).

## Testing

Use [Coverage.py](https://coverage.readthedocs.io/en/6.0.2/) to run the test suite:

```bash
$ coverage run manage.py test
```

You can print a report of the results to your console:

```bash
$ coverage report -m
```
