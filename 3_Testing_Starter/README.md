# Exercise - Testing

In this stage of the app you'll be working in `backend/test_flaskr.py`. Read the inline ToDo comments in the file. In order to run your code, open a new terminal and run: 
```
cd backend
python test_flaskr.py
``` 
The output will looks as: 

```
-------------------
Ran 0 tests in 0.000s
OK
```
### `__init__.py`

Also make sure you read over `/backend/flaskr/__init__.py` file to understand how the solution code is structured. It is an updated file as compared to the last exercise on writing PATCH, POST and DELETE requests. For the current exercise, **no** changes are required in the `__init__.py` file. 

### ToDo - Writing Your Tests
**Write at least two tests for each endpoint - one each for success and error behavior.** To get started, write tests for the *GET /books* endpoint. 

Feel free to write additional tests for nuanced functionality, such as adding a book without a rating, etc. **Since there are four routes currently, you should have at least eight tests.** 

### Start the Application
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

#### Step 3: Complete the ToDos
**Note** that once you run the test to delete a particular book, it will delete that book (book_id) from the database. 

Therefore the same test won't pass again. You can re-run the particular delete book **test with a different book_id**. For your reference, the database has the book_ids from `1` to `16`.

Alternativley, you can repopulate the database anytime by running the following commands from the */nd0044-c2-API-Development-and-Documentation-exercises/3_Testing_Starter/backend/* folder:

```bash
# Linux users
su - postgres bash -c "dropdb bookshelf_test"
su - postgres bash -c "createdb bookshelf_test"
su - postgres bash -c "psql bookshelf_test < /path/to/backend/books.psql"
```

```bash
# Mac users - local workspace
psql postgres
dropdb bookshelf_test
createdb bookshelf_test
psql bookshelf_test < books.psql
```


#### Step 4: Start the backend server
In a new terminal, start your (backend) Flask server by running the command below:
```
cd backend
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
#### Step 5: Test
Again, open a new terminal, and run:
```
cd backend
python test_flaskr.py
```

## Troubleshoot
1. `AssertionError: 422 != 200` <br> You are trying to delete a book that does not exists in the database.

2. `flask.cli.NoAppException` <br> You are running the flask application from the wrong folder. Make sure to run  `flask run` command inside the "backend" folder. 


3. `FATAL:  password authentication failed for user` <br> The database credentials in the `test_flask.py` and `models.py` are not correct. For the workspace, the default username/password is `student/student`. Whereas, for the local implementation, it's `postgres/postgres`.

