from flask import Blueprint, render_template

app_v1 = Blueprint('app_v1', __name__)


@app_v1.route('/')
def app():
    return render_template('index.html', title='Version 1')
