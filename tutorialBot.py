import praw #duh
import time

r = praw.Reddit(user_agent = "Tutorial guy to learn basic Python and programming principles, by Sean /u/MurlockHolmes") # Allows the bot to access reddit, API calls
r.login() # Leaving this blank will prompt me to login whenever the bot is run; if I want it to auto-login, I can pass the USERNAME and PASSWORD as string args

wordsToMatch = ['definantly', 'definently', 'definetly'] # Array of common misspellings of the word definitely
cache = []

def runBot():
    sub = r.get_subreddit("test") # Finds /r/test
    comments = sub.get_comments(limit=25) # Limits bot to 25 calls per second
    for comment in comments:
        commentText = comment.body.lower()
        match = any(string in commentText for string in wordsToMatch)
        if comment.id not in cache and match:
            comment.reply('It looks like you spelled "definitely" wrong, do you want to try again? I am a passive-aggressive robot, please be nice to me')
            cache.append(comment.id)
    print("Bot finished, time for sleep...")

while True:
    runBot() # runs bot
    time.sleep(10) #stops process for 10 seconds