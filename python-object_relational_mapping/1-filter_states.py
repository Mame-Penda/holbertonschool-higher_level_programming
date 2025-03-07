#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    row = curs.fetchall()

    for row in curs:
            if row[1][0] == 'N':
                  print(row)
    curs.close()
    db.close()
