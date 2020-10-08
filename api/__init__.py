from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from api.config import DevConfig, StageConfig, Config, viiru_home_env

app = Flask(__name__)

if viiru_home_env == 'development':
    print('Running VIIRU_HOME in development mode...')
    app.config.from_object(DevConfig)
elif viiru_home_env == 'stage':
    print('Running VIIRU_HOME in staging mode...')
    app.config.from_object(StageConfig)
else:
    print('VIIRU_HOME environment was not found. Please review the configuration variables.')
    print (f'viiru_home_env is {viiru_home_env}')
    app.config.from_object(Config)

# Enable CORS for all resources
CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Flask-Marshmallow is used for serializing the DB objects to JSON.
ma = Marshmallow(app)

from api import routes