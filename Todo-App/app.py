from flask import Flask, render_template, url_for
from flask.wrappers import Request
from icecream import ic
import utils.utils as ut
from model.db_base import DB_BASE

app = Flask(__name__)

ic.configureOutput(includeContext=True)


@app.route('/')
def todo_list_home():
    todoListDB = DB_BASE('todo-list')
    completeTodoList = ic(ut.attachColorClassName(
        todoListDB.fetchCompleteCollection()))
    todoListDB.dbClient.close()
    return render_template('index.html', completeTodoList=completeTodoList)


@app.route('/submit_task', methods=['POST'])
def submit_task():
    todoListDB = DB_BASE('todo-list')
    ic(Request.form)
    todoListDB.dbClient.close()


if __name__ == '__main__':
    app.run(debug=True)
