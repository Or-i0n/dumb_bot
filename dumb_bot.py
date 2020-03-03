"""After pressing RUN, enter your message!"""

from urllib import request
import json
import random


dont_know = ["I don't know", "I don't know about it", "I am still learning",
             "I am just a chat bot",
             "Sorry don't know that", "sometimes I just can't answer",
             "I am not programmed to answer that",
             "Next question", "Move on", "Say something else",
             "I may answer that in my new version",
             "I am just a basic chatbot",
             "This is complex to answer, right now beyond my limit",
             "Ask in simple words"]

url = "https://raw.githubusercontent.com/Or-i0n/dumb_bot/master/parsed_conversation.json"

req = request.urlopen(url)
dataset = json.loads(req.read())

hits = []
usr = input()
queries = usr.lower().split()
print("[USR]:", usr)

if usr:
    for reply in dataset:
        if all(query in reply.lower().split() for query in queries):
            hits.append(reply)
    if hits:
        print("[BOT]:", random.choice(hits))
    else:
        print("[BOT]:", random.choice(dont_know))
else:
    print("[BOT]: Say something!")
