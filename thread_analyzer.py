import requests

API_URL = "https://slack.com/api/conversations.history?token=<APP_TOKEN>&channel=<CHANNEL_ID>&oldest=<UNIX_TIMESTAMP>&latest=<UNIX_TIMESTAMP>"

#Dictionary of members to be checked.
team_members = {"<USER_SLACK_ID>":"<USERNAME>"}
response_counter = 0

r = requests.get(url=API_URL)
data = r.json()

#Loop on every message on the channel.
for message in data["messages"]:
    
    #Check if the message is a thread or not.
    if "thread_ts" in message.keys():
        for thread_response in message["replies"]:

            #Check if listed member is among the thread responders.
            if thread_response["user"] in team_members.keys():
                response_counter += 1
                
                print(f"{team_members[thread_response['user']]} replied on thread --> {message['text']}")

                #Add break to exit the loop. This is to ignore multiple replies on a single thread.
                #Also ignores replies of multiple members. 
                break

print("#########")
print("#########")
print(f"Total thread responses by members: {response_counter}")
