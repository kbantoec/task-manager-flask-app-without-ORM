# Task Manager App (without ORM)

Task Manager App without the `SQLAlchemy` Module.

* `tmapp` stands for **t**ask **m**anager **app**

Workflow:

```powershell
git init
mkdir tmapp
pip list
pip install flask
touch README.md, .gitignore, app.db
cd .\tmapp\
mkdir templates, static, tests
touch __init__.py, views.py, models.py
cd ..
touch .\tmapp\templates\index.html, touch .\tmapp\templates\update.html, touch .\tmapp\templates\base.html
```

With Python to populate the database (typing `python` in the terminal at the root of the project):

```python
>>> from tmapp.models import db
>>> import sqlite3
>>> cur = sqlite3.Cursor(db)
>>> print(cur.fetchall())
```

