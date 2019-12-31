## Thread Analyzer
Guide steps to determine the number of message threads a member/user was involved. (in Slack channels)

###### Usage
**Step 1:** Create Slack App (https://api.slack.com/apps?new_app=1)
For the OAuth Scope, you need to give at least below permissions.
* channels:history
* channels:read

After the creation, you will have your OAuth Token.

**Step 2:** Determine the ID of the Slack channel you'll be checking.
You can use the API with the OAuth Token. (https://slack.com/api/conversations.list?token=<OAuth_Token>)

_Sample Output:_
```
{
  "ok": true,
  "channels": [
    {
      "id": "CRVB5VB9P",   #Channel ID
      "name": "random",    #Channel Name
      "is_channel": true,
```

**Step 3:** Determine the start and end range of your query. (in UNIX timestamp format)
You may use online converters for it.

Sample Output:
January 01, 2020 == 1577836800 #This is the UNIX timestamp format

**Step 4:** Build your API URL
For the start and end range parameters, we will use _oldest_ and _latest_ respectively.

_Sample Output:_
https://slack.com/api/conversations.history?token=<APP_TOKEN>&channel=<CHANNEL_ID>&oldest=<UNIX_TIMESTAMP>&latest=<UNIX_TIMESTAMP>"



**Step 5:** Prepare the Slack ID of members that will be included in the checking.
You can get your Slack ID on Slack by clicking your name --> _Profile and Account_ --> then expand the options, ID is at the bottom part.


**Step 6:** Run the script providing your API URL and a dictionary of members. ("member_id":"member_name")

