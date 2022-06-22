import urllib3
import json
import base64
from rest.conf import *

http = urllib3.PoolManager()
def mpesa_token():
    data_to_encode = f'{conf["CONSUMER_KEY"]}:{conf["CONSUMER_SECRET"]}'
    encoded = base64.b64encode(data_to_encode.encode('utf-8'))
    en=(encoded.decode('ascii'))
    res=http.request(
        method='GET',
        url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
        headers={
            'Authorization': f'Basic {en}',
        }
      )
    data= json.loads(res.data.decode('utf-8'))
   
    return data