import json

def who_trigger_me(event, context):
    try:
        message = f"I'm triggered by {event['Records'][0]['eventSource']} !"
    except KeyError:
        message = f"I'm triggered by {event['Records'][0]['EventSource']} !"
    
    print(message)
    
    body = {
        "message": message,
        "input": event,
    }
    
    return {"statusCode": 200, "body": json.dumps(body)}