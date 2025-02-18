#!/usr/bin/python3
"""Consuming and processing data from an API using Python."""
import requests
import json
import csv


def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints the titles."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetches posts, structures the data, and saves it to a csv file."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        data = [{"id": post["id"], "title": post["title"], "body":
                 post["body"]} for post in posts]

    with open("posts.csv", mode="w", newline="", encoding="utf-8") as csvfile:
        fielnames = ["id", "title", "body"]
        writer = csv.DictWriter(csvfile, fielnames=fielnames)

        writer.writeheader()
        writer.writerows(data)
        print("Data saved to posts.csv")

        if __name__ == "__main__":
            fetch_and_print_posts()
            fetch_and_save_posts()
