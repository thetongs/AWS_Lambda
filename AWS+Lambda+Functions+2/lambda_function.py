
import json

def lambda_handler(event, context):
    # TODO implement
    print('Welcome to my first AWS Lambda Function!')
    if event['Bank Client ID'] == "000":
        print('Bank Client ID 000 corresponds to client name: David Chen')
    elif event['Bank Client ID'] == "001":
        print('Bank Client ID 001 corresponds to client name: Kim Richard')
    elif event['Bank Client ID'] == "002":
        print('Bank Client ID 002 corresponds to client name: Adam Aly')
    else:
        return 'I do not recognize this ID'
     
