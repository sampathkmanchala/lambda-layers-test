
import requests
from faker import Faker
from pyqrcode import create as create_qr_code
from nameparser import HumanName
import json

def lambda_handler(event, context):
    print(f"Version of requests library: {requests.__version__}")
    request = requests.get('https://www.google.com/')
    fake = Faker()
    address = fake.street_address()
    qr_code = create_qr_code('"hellow world"', encoding='utf16')
    print("qr_code:",qr_code)
    name = HumanName("Sir Bob Andrew Dole")
    initials = json.dumps(name.initials_list())

    
    
    return {
        'statusCode': request.status_code,
        'body': {"html":request.text, "address":address, "initials": initials}
    }
