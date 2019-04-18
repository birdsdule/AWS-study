import json
import boto3
import decimal

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    # TODO implement
    bucket = event['Records'][0]['s3']['bucket']['name']  # get the bucket name
    print("buctet is :", bucket)
    json_file_name = event['Records'][0]['s3']['object']['key']  # get the json file name
    if json_file_name == 'moviedata.json':
        json_object = s3_client.get_object(Bucket=bucket, Key=json_file_name)  # get json object
        jsonFileReader = json_object['Body'].read()  # read json file context
        table = dynamodb.Table('Movies')
        movies = json.loads(jsonFileReader.decode('utf-8'), parse_float=decimal.Decimal)#decode json and use decimal to modify float
        for movie in movies:
            table.put_item(Item=movie)
            print("movie added", movie)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
