#!/usr/bin/python3
"""Module for number_of_subscribers function"""

from requests import get


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = get(url, headers={'User-Agent': 'curl'})

    if response.status_code != 200:
        return 0

    response = response.json()
    subscriber_count = response.get('data').get('subscribers')

    return subscriber_count
