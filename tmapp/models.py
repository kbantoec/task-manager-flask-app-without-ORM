from .views import app
import sqlite3
from datetime import datetime

# Start connection with the database (also creates the file if it does not yet exist)
db: sqlite3.Connection = sqlite3.connect(app.config['DATABASE_URI'])
print(db)

# Create a cursor to interact with the database
cursor: sqlite3.Cursor = db.cursor()
print(cursor)


def create_todo_table():
    cursor.execute("CREATE TABLE todo(id INTEGER PRIMARY KEY ASC, content VARCHAR, date_created DATETIME);")
    db.commit()
    db.close()


def test_db():
    cursor.execute("CREATE TABLE todo(id INTEGER PRIMARY KEY ASC, content TEXT, date_created TEXT );")
    # cursor.execute("INSERT INTO `todo` VALUES (?, ?);", ('Hello World!', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')))
    db.commit()
    db.close()


# Create table structure 
# class Todo(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # content = db.Column(db.String(200), nullable=False)
    # date_created = db.Column(db.DateTime, default=datetime.utcnow())

    # def __repr__(self):
    #     return f"'<Task {self.id!r}>'"
