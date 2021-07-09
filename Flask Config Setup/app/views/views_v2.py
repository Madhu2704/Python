from flask import Blueprint, render_template

app_v2 = Blueprint('app_v2', __name__)


@app_v2.route('/')
def app():
    return render_template('index.html', title='Version 2')
