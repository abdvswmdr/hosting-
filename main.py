import praw

reddit = praw.Reddit(
    client_id="aVib-yPvkf_N72ZGeJS4cQ",
    client_secret="Ar4xkXyjcOTFuYop51bZnn6l-N5idA",
    password= "Hehehe12345.",
    user_agent="<console:HAPPY:1.0>",
    username = "abdvswmdr",
 )




import random
import time
def karma():
    try:
        messages = ["Upvoted, upvote in return?",
                "Great post, care to share the upvotes!"]
        for submission in reddit.subreddit("FreeKarma4U+FreeKarma4You").stream.submissions(): 
            submission.upvote()
            rand = random.randint(0, (len(messages)-1))
            print(submission.title)
            submission.reply("Upvoted, upvote in return?")
            time.sleep(80)
    except: 
        time.sleep(300)
        karma()
