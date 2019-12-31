import requests

URL = "https://slack.com/api/conversations.history?token=<APP_TOKEN>&channel=<CHANNEL_ID>&oldest=<UNIX_TIMESTAMP>&latest=<UNIX_TIMESTAMP>"

members = {"<USER_SLACK_ID>":"<USERNAME>"}
counter = 0

r = requests.get(url=URL)
data = r.json()

#Loop on every message on the channel.
for message in data["messages"]:
    
    #Check if the message is a thread or not.
    if "thread_ts" in message.keys():
        for details in message["replies"]:

            #Check if listed member is among the thread responders.
            if details["user"] in members.keys():
                counter += 1
                print(f"{members[details['user']]} replied on thread --> {message['text']}")
                break

print("#########")
print("#########")
print(f"Total thread responses by members: {counter}")
