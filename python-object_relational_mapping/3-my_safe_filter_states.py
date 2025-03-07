#!/usr/bin/python3
"""script that takes in arguments and displays all values in the table"""

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

    # Exécuter la requête pour récupérer tous les états triés par id
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))

    cur.execute(query)
    # Récupérer et afficher les résultats
    for state in cur.fetchall():
        print(state)

    # Fermer le curseur et la connexion à la base de données
    cur.close()
    db.close()
