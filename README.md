# Billing-Counter Backend

Backend system for Billing Counter built on [DRF](https://www.django-rest-framework.org/)

- **local**: http://localhost:/
- **production**: http://54.198.181.201/

## Requirements

##### For running the script

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- Libraries mentioned below

## Cloning

* Create a virtual environment
```bash
python -m venv ./venv
source ./venv/bin/activate
```
* Use `git clone` to clone the repo
```bash
git clone git@github.com:FumaxIN/Billing-Counter.git
```

## Running

* Install the requirements
```bash
  pip install -r requirements.txt
```
* Create a databse 'billing' on psql `createdb psql` and make migrations
```bash
python manage.py migrate
```
* Run server
```bash
python manage.py runserver
```