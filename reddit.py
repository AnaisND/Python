import praw  #Of course after installing PRAW in Command Prompt with "pip install praw" on Windows
import configuration

def logging_in():
    red = praw.Reddit(username=configuration.username,
                password=configuration.password,
                client_id=configuration.client_id,
                client_secret=configuration.client_secret,
                user_agent="Anais's Robot 0.1")
    return red

def running(red):
    for comment in red.subreddit("test").comments(limit=25):
        if "asshole" in comment.body:
            print("Bad word used!")
            comment.reply("This is a bot! Please don't use any bad words!")
            
 #This bot replies to comments on posts from the subreddit "test" with "Please don't use bad words!" whenever somebody comments "asshole".


red = logging_in()
running(red)
