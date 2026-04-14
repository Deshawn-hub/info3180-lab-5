from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .models import db
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config.from_object(Config)

# initialize database
db.init_app(app)

# initialize migrate
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

from app import views