from pprint import pprint
from config import DevConfig, ProdConfig
from app import app
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

if __name__ == '__main__':
    if os.environ.get("ENV") == 'development':
        app.config.from_object('config.DevConfig')
    if os.environ.get("ENV") == 'production':
        app.config.from_object('config.ProdConfig')
    # pprint(app.config)
    app.run(host=app.config['HOST'], port=app.config['PORT'])
