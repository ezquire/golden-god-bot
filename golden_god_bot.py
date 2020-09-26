import praw
import config
import time
import os
import random
from dotenv import load_dotenv
import golden_replies

def bot_login():
    print("Logging in...")
    try:
        r = praw.Reddit(
            client_id = os.getenv("REDDIT_CLIENT_ID"),
            client_secret = os.getenv("REDDIT_CLIENT_SECRET"),
            password = os.getenv("REDDIT_PASSWORD"),
            user_agent = os.getenv("REDDIT_USER_AGENT"),
            username = os.getenv("REDDIT_USERNAME")
        )
        if str(r.user.me()) == "golden_god_bot":
            print("Logged in successfully!")
            return r
    except Exception as e:
        print(e)
    return False


def run_bot(r, comments_replied_to, reply):
    comments = r.subreddit(os.getenv("SUBREDDIT")).comments(limit=1000)
    print(comments)
    for comment in comments:
        if (
            "Golden God" in comment.body or 
            "golden god" in comment.body or 
            "golden God" in comment.body or
            "GOLDEN GOD" in comment.body or
            "Golden god" in comment.body
            ) and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with \"Golden God\" found in comment", comment.id)
                try:
                    comment.reply(reply)
                    print("Replied to comment", comment.id)
                    comments_replied_to.append(comment.id)
                    with open("comments_replied_to.txt", "a") as f:
                        f.write(comment.id + "\n")
                except Exception as e:
                    print(e)
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
    return False


def get_golden_reply():
    if not golden_replies:
        return "MY RAGE IS UNTETHERED AND I KNOW NO BOUNDS!"
    try:
        return random.choice(golden_replies)
    except Exception as e:
        print(e)
    return False


def main():
    load_dotenv()
    r = bot_login()
    comments_replied_to = get_saved_comments()
    reply = get_golden_reply()
    while True:
        run_bot(r, comments_replied_to, reply)


if __name__ == "__main__":
    main()