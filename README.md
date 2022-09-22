# orm-example

## Background

This repository contains a simple example of how data used by a webapp can be persisted in a database and uses this as a motivation for object-relational mapping.

The same simple functionality (providing a list of patients and stations, and information on which patient is in which station in a hospital) is implemented in three separate apps:

* "directsql", where the required data is pulled from the database using SQL queries directly in the views
* "manualorm", where a Patient and Station class are defined that encapsulate database access (still using manually generated SQL queries, but from within the class) so that the views can operate directly on the relevant objects without worrying about queries
* "djangoorm", where the Patient and Station classes derive from Django's Model class, leaving the generation of SQL queries to Django's ORM.

## Installation

This works on Ubuntu 22.04.

### Install prerequisites

```bash
sudo apt-get install -y python3-venv python3-dev git mariadb-server mariadb-client libmariadb-dev
```


### Clone the repository

```bash
git clone https://github.com/dabrowskiw/orm-example.git
```

### Create virtual environment with required python packages

```bash
python3 -m venv ./venv/
source ./venv/bin/activate
pip3 install -r requirements.txt
```

### Setup mariadb

First, secure the database as you always should
```bash
sudo mysql_secure_installation
```

Then, set up the database and user for the orm project. **Caution**: This sets the password from [dbsetup.sql](dbsetup.sql)! Use at your own risk - it is better to locally change the password in [dbsetup.sql](dbsetup.sql) (line 2) and [django/orm/orm/settings.py](django/orm/orm/settings.py) (line 81)!
```bash
sudo mysql -u root -p < dbsetup.sql
```

Then, let django do its own table setups. Go to the directory django/orm (where manage.py is) and run:

```bash
python manage.py migrate
```

### Setup the djangoorm app

In order for the djangoorm app to work, the tables derived from the model need to be applied to the database. Run:

```bash
python manage.py sqlmigrate djangoorm 0001
python manage.py migrate
```

Finally, add the example data to the database by running:

```bash
sudo mysql -u root -p < ormdata.sql
```

## Running

Now, you can run the server using:

```bash
python manage.py runserver
```

Then, you can access the three apps under the following links:

* Direct SQL queries: http://127.0.0.1:8000/directsql/
* Manual ORM: http://127.0.0.1:8000/manualorm/
* Django ORM: http://127.0.0.1:8000/djangoorm/