import praw
import config
import time
import os

def bot_login():
    print ("Logging in...")
    r = praw.Reddit('goldengod')
    if str(r.user.me()) == "golden_god_bot":
        print ("Logged in successfully!")
        return r

def run_bot(r, comments_replied_to, golden_replies):
    print ("Searching last 1,000 comments")
    for comment in r.subreddit('test').comments(limit=1000):
        if ("Golden God" in comment.body or "golden god" in comment.body) and comment.id not in comments_replied_to and comment.author != r.user.me():
            print ("String with \"Golden God\" found in comment", comment.id)
            comment.reply("I AM THE GOLDEN GOD!")
            print ("Replied to comment", comment.id)
            comments_replied_to.append(comment.id)
            with open ("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")
    print ("Search Completed.")
    print (comments_replied_to)
    print ("Sleeping for 10 seconds...")
    #Sleep for 10 seconds...		
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))
        return comments_replied_to

def get_golden_replies():
    if not os.path.isfile("golden_replies.txt"):
        golden_replies = ["MY RAGE IS UNTETHERED AND I KNOW NO BOUNDS!"]
    else:
        with open("golden_replies.txt", "r") as f:
            golden_replies = f.read()
            golden_replies = golden_replies.split("\n")
            golden_replies = list(filter(None, golden_replies))
    return golden_replies

def main():
    r = bot_login()
    comments_replied_to = get_saved_comments()
    golden_replies = get_golden_replies()
    print (comments_replied_to)
    print (golden_replies)
    while True:
        run_bot(r, comments_replied_to, golden_replies)

if __name__ == "__main__":
    main()
