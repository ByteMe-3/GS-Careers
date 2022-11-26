# GS Careers

GS Careers App for promoting Goldman Sachs`s events.

## Installation and Run

Requires [Python3.11](https://www.python.org/) and [docker-compose](https://docs.docker.com/compose/)  to run.

Installing with poetry.

```sh
poetry install
poetry run python manage.py migrate
```

Run with poetry

```sh
docker-compose up -d
poetry run python manage.py runserver
```

Installing with pip and virtualenv.

```sh
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
```

Run with pip

```sh
docker-compose up -d
python manage.py runserver
```

Run with pip

```sh
docker-compose up -d
python manage.py runserver
```

