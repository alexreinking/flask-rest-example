# Flask REST API Example

This is a basic Flask REST API example consisting of a few very simple endpoints.
Please consult the Flask documentation here: https://flask.palletsprojects.com/en/2.1.x/

## Setting up

First, create a virtual environment to manage the project dependencies:

On Windows:

```
> python -m venv venv
> venv\Scripts\activate.bat
```

On Linux:

```
$ python -m venv venv
$ . venv/bin/activate
$ python -m pip install -r requirements.txt
```

## Running the app

From the root directory (the one containing this file), run:

On Windows:

```
> set FLASK_APP=src/flaskr
> flask run
```

On Linux:

```
$ FLASK_APP=src/flaskr flask run
```

## Running the tests

The tests can run by simply running `pytest` at the command line.
