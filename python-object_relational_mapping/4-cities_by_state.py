#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cur = db.cursor()

    # requête SQL pour recupérer les villes avec leur état associé
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
    cur.execute(query)

    # Récupérer et afficher les résultats
    for city in cur.fetchall():
        print(city)

    # Fermer le curseur et la connexion à la base de données
    cur.close()
    db.close()
