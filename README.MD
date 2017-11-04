   # INSTALL

You need to have Python 3 (3.4 or later) installed on your PC,
also you need Python utilities "pip" and "virtualenv".

To launch the django app, you need:

1. cd to a directory of your choice (eg: cd ~/prj)
2. git clone https://github.com/igrik6556/dev_task.git
3. virtualenv dev_task_env --no-site-packages

   a) cd dev_task_env/bin/

   b) . activate

   c) cd ../../

4. cd dev_task
5. pip3 install -r requirements.txt
6. create db in postgres on your local pc. Add db_name, user and password in src.settings.py

    Notes: project comes with some fixture. To add them in your database execute command:

            python3 manage.py loaddata data.json

7. python3 manage.py runserver
8. open http://localhost:8000/ in your browser


# DESCRIBE
You'll need to create NBA stats web app to help gamble people be on teams.

[1] Input Data Creation

To make any computations you'll need input data. In our case, it will be Teams and Players. They should be stored in PostgreSQL as entities.

Team structure:

     {

      "name": "Lakers",

      "city": "Los Angeles"

     }

Player structure:

    {

     "name": "John Ace",

     "age": 25,

     "height": 198,

     "experience": 8,

     "goals": 800,

     "team": 1

    }
This data should be available to create and get through REST API (UI is not necessary). API routes to create:

- POST /team
- POST /player
- GET /teams
- GET /players
- GET /teams/:teamId
- GET /players/:playerId

[2] Statistics

A simple web page which is needed for our app is Statistics.

Statistics represent score table of teams.

Score tables should contain aggregated data by teams, like Goals quantity, team members average stats and team score (calculated by your algorithm). They should be sorted based on this score, so we'll know who we should bet on.
