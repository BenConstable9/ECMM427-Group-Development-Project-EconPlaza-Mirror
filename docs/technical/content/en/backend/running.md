---
title: Running the API
description: ''
position: 230
category: Backend
---

Make sure you have Python 3.9 installed and configured on your system.

Set up and activate a virtual environment:

```bash
$ python -m venv '.env'

$ source .env/bin/activate          # Linux
$ .env/Scripts/activate             # Windows
```

Install the required packages to your environment.:

```bash
$ pip install -r requirements.txt
```

Navigate to the project directory, where `manage.py` is located.

```bash
$ cd backend
```

Set environmental variable to true.

```bash
$ $env:DEVELOPMENT="True"           # Windows Powershell
```

Set up your local database by running migrations:

```bash
$ python manage.py migrate
$ python manage.py createcachetable
```

Create a superuser for admin control of the database

```bash
$ python manage.py createsuperuser
```

Finally, run the server:

```bash
$ python manage.py runserver
```

You can visit it at `http://localhost:8000/` (`http://127.0.0.1:8000/`).

## Testing

```bash
$ pip install -r requirements-test.txt
```

Use [Coverage.py](https://coverage.readthedocs.io/en/6.0.2/) to run the test suite:

```bash
$ coverage run manage.py test
```

You can print a report of the results to your console:

```bash
$ coverage report -m
```

