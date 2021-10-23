# EconPlaza backend (Django)
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
