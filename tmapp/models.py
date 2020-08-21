from .views import app
import sqlite3
from datetime import datetime


def create_todo_table():
    # Start connection with the database (also creates the file if it does not yet exist)
    conn: sqlite3.Connection = sqlite3.connect(app.config['DATABASE_URI'])
    # Create a cursor to interact with the database
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.execute("CREATE TABLE todo(id INTEGER PRIMARY KEY ASC, content TEXT, date_created TEXT );")
    conn.commit()
    conn.close()


class Todo:
    def __init__(self, content: str, id: int = None, date_created: str = None):
        if isinstance(content, str):
            self.content: str = content
        else:
            print(f"Error: {'str'!r} expected, but got {type(content)!r}.")
        
        if (id is None) or (isinstance(id, int)):
            self.id: int = id
        else:
            print(f"Error: {'int'!r} expected, but got {type(id)!r}.")

        if date_created is None:
            self.date_created: str = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(date_created, str):
            self.date_created: str = date_created
        else:
            print(f"Error: {'str'!r} expected, but got {type(date_created)!r}.")

    def __repr__(self):
        return f"<Task {self.id!r}>'"

