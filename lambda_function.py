
import requests
from faker import Faker

def lambda_handler(event, context):
    print(f"Version of requests library: {requests.__version__}")
    request = requests.get('https://www.google.com/')
    address = fake.street_address()
    return {
        'statusCode': request.status_code,
        'body': {"html":request.text, "address":address}
    }
