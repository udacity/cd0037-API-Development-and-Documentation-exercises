# Errors Lab

Now that we have our endpoints, we need to make sure we send back formatted responses when we hit an error. **Pre-requisites and dependencies** are same as the ones explained in the [first exercise's starter code](https://github.com/udacity/nd0044-c2-API-Development-and-Documentation-exercises/blob/master/1_Requests_Starter/README.md)

## ToDo
In `__init__.py` use the `errorhandler` decorator to handle all of the errors used in the endpoints. *Before* you get started make sure you read over the endpoint code and inline comments. 

We have provided code to give you a starting point which you need to review in order to understand the code and errors you'll be working with. 

During this exercise, you'll also notice instructions to use `curl` to write requests. Take this opportunity to do so, such that you have practice before you need to use it in a professional setting! 

## How to run the application
### Step 0: Start/Stop the PostgreSQL server
```bash
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
You will have your database already in place. In case you played around with table and data, you can anytime drop and recreate the database. Refer to the [first exercise's starter code](https://github.com/udacity/nd0044-c2-API-Development-and-Documentation-exercises/blob/master/1_Requests_Starter/README.md) again.

### Step 2 - Start the frontend server
From the `frontend` folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```
By default, the frontend will run on `localhost:3000`. Close the terminal if you wish to stop the frontend server. 

### Step 3 - Complete the ToDos
Open the */backend/flaskr/__init__.py* file, and finish all the @TODOs. 

There is no change in the frontend this time. 

### Step 4 - Start the backend server
In a new terminal, start your (backend) Flask server by running the command below:
```bash
cd backend
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

### Step 5 - Access the app
Now, run the app and test both the services:
1. Backend (flask): http://127.0.0.1:5000/ (use CURL within the workspace)

2. Frontend: You can acces `http://localhost:3000` for the frontend. 
