#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists"""

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
        ORDER BY cities.id ASC, (sys.argv[4],)
        """
    cur.execute(query)

    # Récupérer et afficher les résultats
    for cities in cur.fetchall():
        print(", ".join(city[0] for city in cities))

    # Fermer le curseur et la connexion à la base de données
    cur.close()
    db.close()
