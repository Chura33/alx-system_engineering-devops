#!/usr/bin/python3
""" This module returns the number of subscribers
to a reddit channel"""

import requests


def number_of_subscribers(subreddit):
    res = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"}
    )

    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    else:
        return (0)
