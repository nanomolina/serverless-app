import json
import os
import requests
import futbol


def lambda_handler(event, context):
    telegram_token = os.environ['TELEGRAM_TOKEN']

    api_url = f"https://api.telegram.org/bot{telegram_token}/"


    # Get body as json
    body_str = event.get('body', '')
    body_str = body_str.replace('\\n', r'\\n')
    body = json.loads(body_str)

    # Get chat_id
    message = body.get('message', body.get('edited_message', {}))
    chat_id = message.get('chat', {}).get('id', None)
    # Get team input
    text = message.get('text', 'Default')
    text = text.replace(r'\n', '\n')

    # Run socces algorithm
    try:
        text_response = futbol.print_2_random_soccer_teams(text)
    except Exception as e:
        text_response = 'Try again'

    # Create response
    params = {'chat_id': chat_id, 'text': text_response}
    res = requests.post(f"{api_url}sendMessage", data=params).json()

    if res["ok"]:
        return {
            'statusCode': 200,
            'body': json.dumps(res['result']),
        }
    else:
        print(res)
        return {
            'statusCode': 400,
            'body': json.dumps(res)
        }
