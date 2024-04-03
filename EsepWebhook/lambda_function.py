import json
import os
import urllib.request
import urllib.parse

def lambda_handler(event, context):
    # Get the issue url
    issue_url = event['issue']['html_url']
    
    # Message to be posted to Slack
    slack_message = {
        "text": f"Issue Created: {issue_url}"
    }
    
    # Send the message to Slack
    slack_webhook_url = os.environ['SLACK_URL']
    data = json.dumps(slack_message).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    req = urllib.request.Request(slack_webhook_url, data=data, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)  # response from slack webhook
            return {
                'statusCode': 200,
                'body': json.dumps('Message sent to Slack successfully')
            }
    except urllib.error.HTTPError as e:
        print(e.code, e.reason)  # e
        return {
            'statusCode': e.code,
            'body': json.dumps('Failed to send message to Slack')
        }
