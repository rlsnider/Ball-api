##Steps to Create application
1. create virtual environment
    a.) Python3 -m venv venv
    b.) .\venv\Scripts\activate
2. Install Flask
    a.)pip install Flask
    b.)flask run --reload
3. Create app.py
    a.)import flask (check your route connection, make a temporary simple route)
4. All Good? do a commit
5. Create Application Factory
    a.)make "ball" directory
    b.) in ball dir make __init__.py file
    c.) import flask then make your route app(def create_app())
    d.) erase the temp info in the app.py file and import the ball dir to it.
    e.) check your work in browser
    f.) all good? do a commit
6.  Database Integration with Flask
    a.) Create a database named ballpy with a table named reptiles in pgadmin.
    b.) Install ORM using pip
    c.) Add the config in __init__.py 
7.  Add model
    a.) create a file named models.py in the ballpy folder.
    b.) import Sqlalchemy
    c.) in __init__.py  import models
    d.) in models.py create you model
    e.) install Flask-Migrate and psycopg2-binary
    f.) import the migrate class from the package in __init__.py
    g.)initialize migrations folder by funning flask db migrate
8. Create blueprints and routes
    a.) create reptile.py file in ballpy dir
    b.) import Blueprint from flask, define bp info
    c.) go back to the factory(__init__.py) and import reptile and register blueprint
    d.) test and commit

