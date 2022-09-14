# orm-example

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

Then, set up the database and user for the orm project. **Caution**: This sets the password from [dbsetup.sql](dbsetup.sql)! Use at your own risk - it is better to locally change the password in [dbsetup.sql](dbsetup.sql) and [django/orm/settings.py](django/orm/settings.py) (line 81)!
```bash
sudo mysql -u root -p < dbsetup.sql
```
