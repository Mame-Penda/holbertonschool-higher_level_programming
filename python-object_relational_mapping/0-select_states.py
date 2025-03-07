#!/usr/bin/python3
"""list all states from database"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    row = curs.fetchall()

    for row in curs:
        print(row)
    curs.close()
    db.close()
