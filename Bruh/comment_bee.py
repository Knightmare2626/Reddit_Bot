import praw
import re

reddit = praw.Reddit("bot1")

subreddit = reddit.subreddit("bot_testing_2")

contents = []
with open("bee.txt", "r") as file:
    contents = file.readlines()

for submission in subreddit.hot(limit=3):
    if (re.search("bruh", submission.title, re.IGNORECASE)):
        for word in contents:
            submission.reply(word)
        print("Done :thumbsup: :) ")

#note : need to sanitize bee script before using it 