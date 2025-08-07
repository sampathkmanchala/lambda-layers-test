
import requests
from faker import Faker
from pyqrcode import create as create_qr_code

def lambda_handler(event, context):
    print(f"Version of requests library: {requests.__version__}")
    request = requests.get('https://www.google.com/')
    fake = Faker()
    address = fake.street_address()
    qr_code = create_qr_code('"hellow world"', encoding='utf16')
    print("qr_code:",qr_code)
    
    return {
        'statusCode': request.status_code,
        'body': {"html":request.text, "address":address}
    }
