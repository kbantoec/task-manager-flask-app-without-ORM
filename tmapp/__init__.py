from .views import app

# Tell Flask that we are working with a database
from . import models

# Connect our app to the database
@app.cli.command()
def test_db():
    models.test_db()
