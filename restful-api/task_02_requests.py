#!/usr/bin/python3
"""
Un script Python basique pour récupérer des posts de
JSONPlaceholder en utilisant requests
"""

import requests
import csv


def fetch_and_print_posts():
    """Récupérer les posts et imprimer leurs titres"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Échec de la récupération des posts")


def fetch_and_save_posts():
    """Récupérer les posts et les enregistrer dans un fichier CSV"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        fieldnames = ["id", "title", "body"]
        with open('posts.csv', mode="w", encoding="utf-8",
                  newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({"id": post["id"], "title":
                                 post["title"], "body": post["body"]})
        print("Les posts ont été enregistrés dans 'posts.csv'")
    else:
        print("Échec de la récupération des posts")
