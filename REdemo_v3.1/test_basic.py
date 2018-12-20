#from fixtures.mydb import MyDB

import pytest
import sqlite3


@pytest.fixture(scope="module")
def cur():
    print("setting up")
    # db = MyDB()
    # conn = db.connect("server")
    # curs = conn.cursor()
    with sqlite3.connect("database.db") as db:
        curs=db.cursor()
    yield curs
    curs.close()
    db.close()
    print("closing DB")

def test_database_connectivity(cur):
    cur.execute("select User_ID from user where username='atul'")
    id=cur.fetchall()
    assert id[0][0] == 2


