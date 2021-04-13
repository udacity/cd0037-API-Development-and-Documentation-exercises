# Local Development 
The instructions below are meant for the local setup only. The classroom workspace is already set for your to start practicing. 

#### Pre-requisites
* Developers using this project should already have Python3, pip and node installed on their local machines.
* **Install dependeencies**<br>
From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file. 


## How to run the application

### Step 1 - Initial setup
1. Open a new terminal window. From within the project directory, run the below code once:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
```

2. There is a setup script in the project directory. Open a terminal in this Workspace and run the script with:
```
bash setup.sh
```
The script installs the Python dependencies needed for this lab, starts the PostgreSQL service and executes the commands needed to set up the database. You should only need to run this script once.


### Step 2: Complete the ToDos and Start the backend server
Navigate to the `/backend/flaskr/__init__.py` file, and finish all the `@TODO` thereby building out the necessary routes and logic to get the backend of your app up and running.

Once you've written your code, start your (backend) Flask server by running the command below from the `/backend/` directory.
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application is run on `http://127.0.0.1:5000/` by default and is set as a proxy in the frontend configuration. Also, the current version of the application does not require authentication or API keys. 



### Step 3: Start the frontend
(You can start the frontend even before the backend is up!)
From the `frontend` folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```
By default, the frontend will run on `localhost:3000`. Close the terminal if you wish to stop the frontend server. 

---

## Additional information
#### Running Tests
If the current exercise needs testing, navigate to the backend folder and run the following commands: 
```
dropdb bookshelf_test
createdb bookshelf_test
psql bookshelf_test < books.psql
python test_flaskr.py
```
The first time you run the tests, omit the `dropdb` command. All tests are kept in that file and should be maintained as updates are made to app functionality. 


#### Error Handling
- Response codes
- Messages
- Error types

#### Endpoints 
- Organized by resource
- Include each endpoint
- Sample request 
- Arguments including data types
- Response object including status codes and data types 