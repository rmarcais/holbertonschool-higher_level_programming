#!/usr/bin/python3
"""Consuming and processing data from an API using Python"""

import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder"""

    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        for post in r.json():
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder
    and saves them in a CSV file
    """

    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        post_list = []
        for post in r.json():
            post_list.append({"id": post["id"],
                              "title": post["title"],
                              "body": post["body"]})

        fields = ["id", "title", "body"]

        with open("posts.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(post_list)
