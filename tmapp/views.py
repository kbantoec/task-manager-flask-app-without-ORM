from flask import Flask, render_template, request, redirect
from datetime import datetime
from . import utils
import sys
import os
import sqlite3

app = Flask(__name__)

# Load the config variables to our app
app.config.from_object('config')
from .models import Todo
# app.config['DATABASE_URI'] => C:\Users\YBant\Documents\projects\flaskapp_taskmanager_without_orm\app.db

# The way we want to represent our data
# conn.row_factory = dict_factory


@app.route('/', methods=['GET', 'POST'])
def index():
    # Start connection with the database (also creates the file if it does not yet exist)
    conn: sqlite3.Connection = sqlite3.connect(app.config['DATABASE_URI'])

    # Create a cursor to interact with the database
    cursor: sqlite3.Cursor = conn.cursor()

    if request.method == 'POST':       
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        # Push it to our database
        try:
            # You can use a `NULL` to have SQLite insert an auto-generated id for you
            cursor.execute("INSERT INTO `todo` VALUES (NULL, ?, ?);", (new_task.content, new_task.date_created))
            # Save (commit) the changes
            conn.commit()
            conn.close()
            # Redirect to the index
            return redirect('/')
        except Exception as e:
            conn.close()
            print(f"There was a problem adding your task. Error: {e}.", file=sys.stderr)

    else:
        # List of tuples
        tasks_result: list = cursor.execute("SELECT * FROM `todo`;").fetchall()
        tasks: list = [Todo(content=tup[1], id=tup[0], date_created=tup[2]) for tup in tasks_result]
        conn.close()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:identifier>')
def delete(identifier):
    # task_to_delete = cursor.execute("DELETE FROM `todo` WHERE id = (?);", (identifier, ))

    try:
        # Start connection with the database (also creates the file if it does not yet exist)
        conn: sqlite3.Connection = sqlite3.connect(app.config['DATABASE_URI'])

        # Create a cursor to interact with the database
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("DELETE FROM `todo` WHERE id = (?);", (identifier, ))
        conn.commit()
        conn.close()
        return redirect('/')
    except Exception as e:
        print(f"There was a problem deleting your task. Error: {e}.", file=sys.stderr)


@app.route('/update/<int:identifier>', methods=['GET', 'POST'])
def update(identifier):
    # Start connection with the database (also creates the file if it does not yet exist)
    conn: sqlite3.Connection = sqlite3.connect(app.config['DATABASE_URI'])
    conn.row_factory = utils.dict_factory

    # Create a cursor to interact with the database
    cursor: sqlite3.Cursor = conn.cursor()
    
    res: dict = cursor.execute("SELECT * FROM `todo` WHERE id = (?);", (2, )).fetchone()
    task: Todo = Todo(**res)

    if request.method == 'POST':
        task_content = request.form['content']        
        try:
            cursor.execute("UPDATE `todo` SET content = (?) WHERE id = (?);", (task_content, identifier))
            conn.commit()
            conn.close()
            return redirect('/')
        except Exception as e:
            conn.close()
            print(f"There was a problem updating your task. Error: {e}.", file=sys.stderr)
    else:
        conn.close()
        return render_template('update.html', task=task)
   