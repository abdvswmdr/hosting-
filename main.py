import praw 

reddit = praw.Reddit(
    client_id = "7i66SjwRcRKHNNaSlRr1GA", 
    client_secret = "adBGWPi8VW6rXpefr_iJC9o4qIazfQ", 
    password = "Hehehe12345.", 
    user_agent = "<console:HAPPY:1.0", 
    username = "Abdvswmdr-2047"
    
    )

import random
import time 
def karma(): 
    try:
        messages = ["Upvoted! Upvote in return?", 
                    "Great post, care to share the upvotes!", 
                    "Just upvoted you, would you mind upvoting in return!"]
        for submission in reddit.subreddit("FreeKarma4U+FreeKarma4You").stream.submissions():
            submission.upvote()
            rand = random.randint(0, (len(messages)-1))
            print(submission.title)
            submission.reply(messages[rand])
            time.sleep(150)
    except:
        time.sleep(800)
        karma()
karma()
                
