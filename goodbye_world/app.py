import json

def goodbye_fn(event, context):
    name = event.get("queryStringParameters") or {}
    name = name.get("name", "mundo")

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Adiós {name}!", "input": event})
    }