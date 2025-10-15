import json

def lambda_handler(event, context):
    val = event.get("value", 0)
    return {"statusCode": 200, "body": {"processed": val * 2}}
