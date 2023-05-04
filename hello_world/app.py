import json

# import requests


def lambda_handler(event, context):
    a=int(event([queryStringParameters]["a"]))
    b=int(event([queryStringParameters]["b"]))

    return {
        "statusCode": 200,
        "body":Str(a+b)
    }
