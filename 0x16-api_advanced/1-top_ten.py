#!/usr/bin/python3
""" This module prints the titles of the top ten posts in a
given subreddit"""

import requests


def top_ten(subreddit):
    """ This function gets the title of the ten hottests posts"""

    res = requests.get(
            "https://www.reddit.com/r/{subreddit}/hot.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            params={"limit": 10},
    )

    if res.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            obj = get_data.get("data")
            title = get_data.get("title")
            print(title)
    else:
        print(none)
