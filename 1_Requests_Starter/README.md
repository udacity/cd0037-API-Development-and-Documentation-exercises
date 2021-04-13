# Local Development 
The instructions below are meant for the local setup only. The classroom workspace is already set for your to start practicing. 

#### Pre-requisites
* Developers using this project should already have Python3, pip and node installed on their local machines.

* **Install dependencies**<br>
From the backend folder run `pip3 install requirements.txt`. All required packages are included in the requirements file. In addition, you will need the following:
```
pip3 install flask_sqlalchemy
pip3 install flask_cors
pip3 install flask --upgrade
pip3 uninstall flask-socketio -y
```


### Step 0: Start/Stop the PostgreSQL server
```bash
which postgres
postgres --version
# Start/stop
pg_ctl -D /usr/local/var/postgres start
pg_ctl -D /usr/local/var/postgres stop 
```
If it shows that the *port already occupied* error, run:
```bash
sudo su - 
ps -ef | grep postmaster | awk '{print $2}'
kill <PID> 
```

### Step 1 - Create and Populate the database
1. Replace all occurances of the user `xyz` in the `/nd0044-c2-API-Development-and-Documentation-exercises/1_Requests_Starter/backend/books.psql` with your active username or `student`. We will run this .psql script. 

2. In your terminal, navigate to the */nd0044-c2-API-Development-and-Documentation-exercises/1_Requests_Starter/backend/* directory, and run the following:
```bash
# Connect to the PostgreSQL
psql postgres
#View all databases
\l
# Create the database, create a user - `student`, grant all privileges to the student
\i setup.sql
# Exit the PostgreSQL prompt
\q
# Populate the bookshelf database and apply contraints
psql -f books.psql -U student -d bookshelf
```


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