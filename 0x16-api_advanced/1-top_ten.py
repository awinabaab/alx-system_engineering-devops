#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts \
        listed for a given subreddit."""

from requests import get


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts \
            listed for a given subreddit."""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    response = get(url, headers={'User-Agent': 'curl'})

    if response.status_code != 200:
        print(None)

    else:
        response = response.json()

        posts = response.get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
