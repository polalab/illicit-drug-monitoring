"""
This file should be used for implementing scraping data from social media.
Currently, it is implemented to scrape top comments from subreddits specified in file info.py
If you run this file csv files with comments will be generated.
"""
import json
import praw
import pandas as pd


def read_reddit_credentials():
    f = open('credentials.json')
    data = json.load(f)
    reddit_credentials = data['reddit_credentials'][0]
    return reddit_credentials


def create_reddit_object():
    reddit_credentials = read_reddit_credentials()
    reddit = praw.Reddit(client_id=reddit_credentials["client_id"],
                         client_secret=reddit_credentials["client_secret"],
                         user_agent=reddit_credentials["user_agent"],
                         username=reddit_credentials["username"],
                         password=reddit_credentials["password"])
    return reddit


def reddit_scrape(subread_name):
    reddit = create_reddit_object()
    comments = set()
    subred = reddit.subreddit(subread_name)
    hot = next(subred.top())

    for comment in hot.comments:
        comment_body = comment.body
        if comment_body != "[removed]" or comment_body != "[deleted]":
            comments.add(comment.body)

    df = pd.DataFrame(comments)
    df.head()
    out_file_name = 'comments_' + subread_name + '.csv'
    df.to_csv(out_file_name, index=False, encoding='utf-8', header=False)


if __name__ == '__main__':
    info = open('info.json')
    data = json.load(info)
    subread_names = data['subread_names']
    for subread_name in subread_names:
        reddit_scrape(subread_name)
