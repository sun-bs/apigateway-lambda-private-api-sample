import json


def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        return {
            "statusCode": 200,
            "body": json.dumps({
                "yourGetRequest": event['pathParameters']['arg']
            })}

    if event['httpMethod'] == 'POST':
        return {
            "statusCode": 200,
            "body": json.dumps({
                "yourPostRequest": event['body'],
            })}

    return {
            "statusCode": 404,
            "body": "NOT FOUND"
            }
