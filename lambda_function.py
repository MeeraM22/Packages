import boto3
import json
import requests
# from botocore.vendored import requests
def lambda_handler(event, context):

    # TODO implement
    url='https://portal.cognizant-1facility.com/energy-management/energy/system'
    response=requests.get(url)
    print(response.text)

    return 'success'

lambda_handler (1,2)