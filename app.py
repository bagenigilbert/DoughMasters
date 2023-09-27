# Import the Flask framework for creating the web application
from flask import Flask
import os


# Import SQLAlchemy for database management
from flask_sqlalchemy import SQLAlchemy

# Import Flask-Migrate for database migrations
from flask_migrate import Migrate

# Create a Flask web application instance
app = Flask(__name__)

# Configure the database URI (SQLite in this case) for the application
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for performance

db = SQLAlchemy(app)
# postgres://doughmasters_dough_user:Q7MyavxlEaMqbEfV95zG89Ny6uT1mjZL@dpg-cka07cev3ddc739ho85g-a.oregon-postgres.render.com/doughmasters_dough
# Create a Migrate instance to handle database migrations
migrate = Migrate(app, db)

# Import routes (assuming you have route definitions in a 'routes.py' file)
from routes import *

# Run the Flask application in debug mode on port 5003
if __name__ == '__main__':
    app.run(debug=True, port=5007)
