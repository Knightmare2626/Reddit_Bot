import praw

reddit = praw.Reddit("bot1")
subreddit = reddit.subreddit("bot_testing_2")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    # print("Selftext: ", submission.selftext)
    print("Score: ", submission.score)
    print("----------------------------\n")

