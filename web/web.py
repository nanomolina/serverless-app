import json
import futbol


def lambda_handler(event, context):
    # Run socces algorithm
    body_str = event.get('body', '')
    body_str = body_str.replace('\\n', r'\\n')
    body = json.loads(body_str)
    team = body.get('team', [])
    try:
        response = futbol.print_2_random_soccer_teams(team)
    except Exception:
        response = 'Try again'
    return {
        'statusCode': 200,
        'body': json.dumps(response),
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
    }
