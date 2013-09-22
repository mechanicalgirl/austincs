austincs
========

Install
-------

+ create your own local copy of the project

git clone https://github.com/mechanicalgirl/austincs.git

+ cd into the austincs folder

cd austincs

+ install pip and virtualenv

sudo easy_install pip

[sudo] pip install virtualenv

+ create and activate the virtual environment

virtualenv csta_env

source csta_env/bin/activate

+ install requirements

pip install -r requirements.txt

Settings
--------

+ create the db folder and change its permissions

mkdir db

chmod 777 db

+ modify the settings file (csta_project/settings.py) to edit the path to the database file

The value for DATABASES['NAME'] should be '/your/path/to/austincs/db/db'

(Note: in that path, the first 'db' is the folder you just created, the second 'db' is the SQLite database file, which will be created when you run the command below)

+ create the database tables

python manage.py syncdb

Launch the site
---------------

+ start runserver

python mange.py runserver

+ check the site in your browser

http://127.0.0.1:8000/
