#!/usr/bin/python3
"""list all cities of states with the name of states"""
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
    curs.execute("SELECT cities.name "
                 "FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "WHERE states.name = %s"
                 "ORDER BY cities.id ASC", (sys.argv[4],))
    row = curs.fetchall()
    print(", ".join([city[0] for city in row]))
    curs.close()
    db.close()
