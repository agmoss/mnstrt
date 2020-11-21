# `mnstrt`

> Automated rental data collection and storage

## Table of Contents

- [Scope](#scope)
- [Design](#design)
- [Usage](#Usage)
- [Database](#database)
- [Requirements](#requirements)
- [Format](#format)
- [License](#license)

## Scope

The goal of this project is to create an automated rental listing collector. Data is to be gathered for multiple cities and organized in a time series fashion. Results need to be stored persistently for analysis.

## Design

This codebase is written in python and managed via [venv](https://docs.python.org/3/tutorial/venv.html).

## Usage

1. Create venv

```bash
python3 -m venv env
```

2. Activate venv

- unix

```bash
source env/bin/activate
```

- windows

```bash
env\Scripts\activate.bat
```

## Database

This project uses postgres as a database

```sql
CREATE DATABASE mnstrt;
CREATE USER mnstrtuser WITH ENCRYPTED PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE mnstrt TO mnstrtuser;
ALTER ROLE mnstrtuser superuser;
```

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
pylint ./
```

## License

UNLICENSED
