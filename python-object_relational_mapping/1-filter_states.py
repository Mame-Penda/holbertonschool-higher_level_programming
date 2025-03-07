#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)"""

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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    # Récupérer et afficher les résultats
    for state in cur.fetchall():
        print(state)

    # Fermer le curseur et la connexion à la base de données
    cur.close()
    db.close()
