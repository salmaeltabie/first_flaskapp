FLASKAPP

## Table of Contents
***
1. [General Info]
2. [Technologies]
3. [Installation]
***

## General Info
***
This is a simple Flask Application that contains three routes:

The first route: Accepts GET requests and displays a webpage containg "Hello World!" message

The second route: Accepts POST requests and checks a payload message of json type if it has the world "Hello" and respons with either the payload was recieved correctly or not in json format

The third route: Accepts POST requests and check a payload message of form-data type if it has the world "Hello" and respons with either the payload was recieved correctly or not in html format
***

## Technologies
***
A list of technologies used within the project:
* [Python](https://www.python.org/): Version 3.7.9 
* [Flask](https://flask.palletsprojects.com/): Version 2.0.0.dev
***

## Installation
***
-mkdir projectname

-cd projectname

-py -3 -m venv venv

-venv\Scripts\activate

-pip install Flask

-write the app and save it to hello.py

-set FLASK_APP=hello.py

-set FLASK_ENV=development

-flask run

-set FLASK_ENV=development
***
