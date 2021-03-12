# CS5293SP21-PROJECT0
**DEVELOPER**: VIDYADHARI MADDUKURI

This repository contains all required code base to execute project0 requirements.

Following are the details of each function that is used in this project to extract, transform and load the incidents data.

#### 1. fetchIncidentsData(url)
    It takes the url of the data as an input and creates an object that is used to read the data from norman webserver.
#### 2. extractIncidentsData(data)
    It takes a data object as input and returns final transformed data in the form of a pandas data frame.
#### 3. createdb(db)
    This method requires a database name as input and creates the required incidents data in SQLLite database.
#### 4. populatedb(db, incidents_df)
    This method required the database name and the final incidents dataframe as input. Finally it loads data into the incidents table.
#### 5. getStatus
    This method connects to the incidents table, reads the data from table and prints data in desired format (list of alphabetically ordered  nature of incidents and the number of times they have occurred and are separated by the pipe character (|)).

## steps to install required dependencies:
    1. Create a python virtual environment using pipenv
        a. pip install pipenv - installs pipenv package that is used to create python virtual environment
        b. To install any python dependency we have two options
            1. pipenv install <PACKAGE_NAME> - This will install any dependency in python virtual environment and creates 
               Pipfile, which will contain all required dependencies for our project
            2. If the project already contains Pipfile then to install all required dependencies for that project you can use
                the dependencies mentioned in the Pipfile using **pipenv run** command. This will install all required dependencies and 
                your python process.
        c. pipenv creates a Pipfile.lock file to maintain and lock python dependencies for that pipenv environment.
        d. To run a python process in pipenv virtual environment use **pipenv run** command.

## Running code
    1. git clone git@github.com:Vidyadhari6/cs5293sp21-project0.git
    2. cd cs5293sp21-project0/
    3. git checkout tags/v1.0
    4. pip install pipenv
    5. pipenv install
    6. pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf

## Running unit test
    pipenv run pytest