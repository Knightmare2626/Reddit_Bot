import praw

reddit = praw.Reddit("bot1")
subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=10):
    print("Title: ", submission.title)
    # print("Selftext: ", submission.selftext)
    print("Score: ", submission.score)
    print("----------------------------\n")