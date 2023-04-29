# Module 3.7 Assignment
serverless-app-assignment-3.7-liau

## Requirements
For this assigment there are 2 things to be accomplished:

1. Create a new serverless application
2. Create 2 events that will invoke this serverless application

## Create serverless application
The main objective of this assignment is to about the invocation of serverless application by event trigger. As such I'm going to create a very simple servereless application with Python. This application will simply print out the source of the event it recieved. This will demostrate that the serverless is indeed invoked by the 2 events that will be created.

### handler.py
```python
import json

def who_trigger_me(event, context):
    body = {
        "message": f"I'm triggered by {event['Records'][0]['EventSource']} !",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
```
### serverless.yml
```yml
service: serverless-app-assignment-3dot7-liau

frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.9
  region: ap-southeast-1

functions:
  who_trigger_me:
    handler: handler.who_trigger_me
```

### Deploying the application
```
$ serverless deploy

Deploying serverless-assignment-3dot7-liau to stage dev (ap-southeast-1)

✔ Service deployed to stack serverless-assignment-3dot7-liau-dev (86s)

functions:
  who_trigger_me: serverless-assignment-3dot7-liau-dev-who_trigger_me (1.5 kB)
```

### Adding S3 bucket event trigger
`S3 bucket` is added as the first tigger. The application will be invoke whenever a file is being uploaded to S3 bucket

![image](https://user-images.githubusercontent.com/22501900/235310851-e400c503-70c2-48c1-a906-dcfb5ca6eda9.png)

The `Log events` shows that the application was invoked by S3 bucket

![image](https://user-images.githubusercontent.com/22501900/235311852-0653a324-550b-4c2c-9517-717bf94c509c.png)

### Adding SNS event trigger
`Simple Notification System (SNS)` is added as the second trigger. The application will be invoke whenever a message is publish to the SNS topic.

![image](https://user-images.githubusercontent.com/22501900/235312134-40b8ad45-7023-4075-8111-880e33a3b123.png)

![image](https://user-images.githubusercontent.com/22501900/235312256-c03cafea-c801-4452-b896-2d4e00a5ed01.png)

The `Log events` shows that the application was invoked by SNS

![image](https://user-images.githubusercontent.com/22501900/235312555-d1e5b0c8-b1a5-4dbe-95cc-35e04e84203b.png)



