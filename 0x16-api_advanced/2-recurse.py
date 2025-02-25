#!/usr/bin/python3
"""recurse function module"""

from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list containing the titles \
            of all hot articles for a given subreddit."""

    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after
                                                                 )

    response = get(url, headers={'User-Agent': 'curl'}, allow_redirects=False)
    if response.status_code != 200:
        return None
    response = response.json()

    posts = response.get('data').get('children')
    for post in posts:
        title = post.get('data').get('title')
        hot_list.append(title)

    after = response.get('data').get('after')
    if after:
        recurse(subreddit, hot_list, after)

    return hot_list
