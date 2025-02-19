#!/usr/bin/python3
"""Consuming and processing data from an API using Python."""
import requests
import csv

response = requests.get("https://jsonplaceholder.typicode.com/posts")
statuscode = response.status_code


def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints the titles."""
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetches posts, structures the data, and saves it to a csv file."""
    if response.status_code == 200:
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in response.json():
                writer.writerows([{key: post[key] for key in fieldnames}])
