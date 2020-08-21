from tmapp import app


if __name__ == '__main__':
    app.run(debug=True)
    # print(app.config['DATABASE_URI'])
    # import sqlite3
    # from tmapp import utils
    # conn: sqlite3.Connection = sqlite3.connect(app.config['DATABASE_URI'])
    # conn.row_factory = utils.dict_factory
    # cursor: sqlite3.Cursor = conn.cursor()
    # row: dict = cursor.execute("SELECT * FROM `todo` WHERE id = (?);", (2, )).fetchone()
    # print(row)
    # for row in cursor.execute("SELECT * FROM `todo` WHERE id = (?);", (2, )):
    #     print(row)
