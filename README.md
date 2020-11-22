# `mnstrt`

> Automated rental data collection and storage

## Table of Contents

- [Scope](#scope)
- [Design](#design)
- [Structure](#structure)
- [Usage](#Usage)
- [Database](#database)
- [Requirements](#requirements)
- [Format](#format)
- [License](#license)

## Scope

The goal of this project is to create an automated rental listing collector. Data is to be gathered for multiple cities and organized in a time series fashion. Results need to be stored persistently for analysis.

## Design

This codebase is written in Python 3.8.5 and managed via [venv](https://docs.python.org/3/tutorial/venv.html). This codebase is both a collection of useful python functions as well as a [CLI](https://click.palletsprojects.com/en/7.x/) program. If required, the python functions can be extracted from the codebase and used in a notebook environment.

## Structure

```bash
mnstrt/
├── mnstrt/
    ├── mnstrt.py # CLI entry point
    ├── analysis/  # Query data into dataframe
    ├── database/    # Database utils
    ├── fetch_store/   # access and store data

```

## Usage

### Create venv

```bash
python3 -m venv env
```

### Activate venv

- unix

```bash
source env/bin/activate
```

- windows

```bash
env\Scripts\activate.bat
```

### Run CLI

```bash
python -m mnstrt -opt <collect|collect_schedule|test_connection|create_table|analysis>
```

#### CLI Options

- collect: One off data collection and storage
- collect_schedule: Daily collection and storage
- test_connection: Verify successful database setup
- create_table: Create the `rental_data` table
- analysis: Query all data in database into a pandas dataframe

## Database

This project uses postgres as a database

```sql
CREATE DATABASE mnstrt;
CREATE USER mnstrtuser WITH ENCRYPTED PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE mnstrt TO mnstrtuser;
ALTER ROLE mnstrtuser superuser;
```

After creating the database and user populate a `database.ini` file with the necessary values

## Requirements

Project dependencies are managed via pip and requirements.txt

- Generate requirements.txt

```bash
pip freeze > requirements.txt
```

## Format

Formatting via [black](https://github.com/psf/black)

```bash
black ./
```

Linting via [pylint](https://www.pylint.org/)

```bash
pylint ./mnstrt
```

## License

UNLICENSED
