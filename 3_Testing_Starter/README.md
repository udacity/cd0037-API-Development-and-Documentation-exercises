# The Great Bookshelf of Udacity

This project is a virtual bookshelf for Udacity students. Students are able to add their books to the bookshelf, give them a rating, update the rating and search through their book lists. As a part of the Fullstack Nanodegree, it serves as a practice module for lessons from Course 2: API Development and Documentation. By completing this project, students learn and apply their skills structuring and implementing well formatted API endpoints that leverage knowledge of HTTP and API development best practices. 

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/). 

## Student Guidelines

Hello students! You'll use this base in various workspaces throughout the course to build the project incrementally as you expand your skills. At each stage, there will be various 'TODO's marked for you to complete. You'll also notice some TODOs in the frontend section. You should referene those sections for formatting your endpoints and responses, and update the frontend to match the endpoints you choose and the programmed behavior. 

You should feel free to expand on the project in any way you can dream up to extend your skills. For instance, you could add additional book information to each entry or create individual book views including more information about the book, your thoughts or when you completed it. 

## Getting Started

### Pre-requisites and Local Development 
Developers using this project should already have Python3, pip and node installed on their local machines.

#### Backend

From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file. 

To run the application run the following commands: 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration. 

#### Frontend

From the frontend folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```

By default, the frontend will run on localhost:3000. 

### Tests
In order to run tests navigate to the backend folder and run the following commands: 

```
dropdb bookshelf_test
createdb bookshelf_test
psql bookshelf_test < books.psql
python test_flaskr.py
```

The first time you run the tests, omit the dropdb command. 

All tests are kept in that file and should be maintained as updates are made to app functionality. 


## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

### Error Handling
- Response codes
- Messages
- Error types
### Endpoints 
- Organized by resource
- Include each endpoint
- Sample request 
- Arguments including data types
- Response object including status codes and data types 

## Deployment N/A

## Authors
Yours truly, Coach Caryn 

## Acknowledgements 
The awesome team at Udacity and all of the students, soon to be full stack extraordinaires! 

