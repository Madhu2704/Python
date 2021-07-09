
from flask import Flask
from app.views.views_v1 import app_v1
from app.views.views_v2 import app_v2

app = Flask(__name__)

app.register_blueprint(app_v1, url_prefix='/v1')
app.register_blueprint(app_v2, url_prefix='/v2')
