cd ../src
set FLASK_APP=app.py
export FLASK_ENV=development
export SCRIPT_ENV=development
flask db migrate
flask db upgrade
python db_seed.py
