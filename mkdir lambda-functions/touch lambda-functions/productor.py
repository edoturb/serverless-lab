import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('lambda')
    data = {"message": "Hola", "value": 10}
    resp = client.invoke(
        FunctionName="ConsumidorFuncion",
        InvocationType="RequestResponse",
        Payload=json.dumps(data)
    )
    result = json.loads(resp['Payload'].read())
    return {"statusCode": 200, "body": result}
