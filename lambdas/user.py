import json


def get_user(event, context):

    input_id = event.get('pathParameters', {}).get('id', None)

    body = {
        "message": f"The ID introduced was: {input_id}",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
