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


def count_words(subreddit, word_list):
    """Parses the title of all hot articles, and prints a sorted count of \
    given keywords (case-insensitive, delimited by spaces"""

    hot_list = recurse(subreddit)
    if not hot_list:
        return

    word_count = {}
    word_list = [word.lower() for word in word_list]
    hot_list = [title.lower() for title in hot_list]

    for word in word_list:
        for title in hot_list:
            if word in title:
                if word in word_count.keys():
                    word_count[word] += title.count(word)
                else:
                    word_count[word] = title.count(word)

    sorted_count = dict(sorted(word_count.items(),
                               key=lambda item: (-item[1], item[0]),
                               )
                        )
    for k, v in sorted_count.items():
        print('{}: {}'.format(k, v))
