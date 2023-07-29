# Troy-backend
This backend is api services for Chinese - English translating and comparing documents for lawyers

<br />

##  `Flask API Backend` Features

- Stack: `Flask` / `Flask-RestX` / **SQLite** 
- **DB Layer**: `SqlAlchemyORM`, `SQLite` persistence
- **Auth**: JWT tokens managed via `Flask-jwt_extended`
<br />

### Versioning

> **Python** - Python 3.10.6

### Get Started

> **Step 1** - Change the directory to `Troy-backend`

```bash
$ cd Troy-backend
```

<br >

> **Step 2** - Install dependencies using a `virtual environment`

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ pip install -r requirements.txt
```

<br />

> **Step 3** - Setup the `Flask` environment 

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
// OR 
$ (Windows CMD) set FLASK_APP=run.py
$ (Windows CMD) set FLASK_ENV=development
// OR
$ (Powershell) $env:FLASK_APP = ".\run.py"
$ (Powershell) $env:FLASK_ENV = "development"
```

<br />

> **Step 4** - Start the API server (development mode)

```bash
$ flask run
```

Use the API via `POSTMAN` or `Swagger Dashboard` at `localhost:5000`.

<br /> 
