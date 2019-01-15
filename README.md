# Vector Dashboard
A webapp + REST api for controlling your Anki Vector robot friend.

## What's this all about?
REST api's are awesome and let a lot more people have access to their vector's
from many more languages. This project is meant to provide two things:

1) A REST api that mirrors the vector Python API as closely as possible
2) A webapp frontend for controlling the vector remotely

## Docs
This application uses swagger-ui to generate beautiful interactive REST api 
documentation. Just go to http://localhost:5000/docs to test out API calls on
your vector (while running the application, of course).

## Running the application:
#### The fast way, docker:
1) Set up your vector
py -m anki_vector.configure  
and follow instructions to set up your vector

2) build and run the server:  
$ docker-compose build && docker-compose up

3) Access via browser http://localhost:5000/docs and you are good to go :)

#### The less fast way, python:
1) use pip to install the requirements of the server:  
$ pip install -r requirements.txt  
Obs.: I highly recommend to use a virtual env to avoid dependency conflicts.

2) change directory to static folder:  
$ cd static

3) install front end dependencies:  
$ npm install  
(dev-only):  
$ npm i webpack --save-dev  
$ npm i babel-core babel-loader babel-preset-es2015 babel-preset-react --save-dev  
$ npm i react react-dom --save-dev

4) build the front end:  
$ npm run build  
Obs.: You can use 'npm run watch' to avoid building the front end everytime a change is made.

5) change to main directory:  
$ cd ..

6) Set up your vector
py -m anki_vector.configure  
and follow instructions to set up your vector

7) run the server:  
$ uwsgi uwsgi.ini

8) Access via browser http://localhost:5000/docs and you are good to go :)

## About
#### Main Technologies:
* Python
* pip
* Flask
* Javascript
* ReactJS
* NPM
* webpack
* CSS
* Docker
* Swagger UI

#### Creating the swagger.json
I currently use [this website](https://app.swaggerhub.com) to build my API docs.
If you would like to contribute to this project, I can share you in on it. 