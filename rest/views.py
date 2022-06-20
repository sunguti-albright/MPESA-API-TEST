import imp
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .conf import *

import json
import base64
import urllib3
import pybase64

http = urllib3.PoolManager()    
# r = http.request(
#     'GET',
#     'http://httpbin.org/headers',
#     headers={
#         'X-Something': 'value'
#     }
# )
# json.loads(r.data.decode('utf-8'))['headers']
# {'X-Something': 'value', ...}

# Create your views here.
@api_view(['GET'])
def get_mpesa_auth(request):
    print(request.method)
    #encoding the consumer key and consumer secret
    data_to_encode = f'{conf["CONSUMER_KEY"]}:{conf["CONSUMER_SECRET"]}'
    print(data_to_encode)
    encoded = base64.b64encode(data_to_encode.encode('utf-8'))
    
    res=http.request(
        method='POST',
        url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
        headers={
            'Authorization': f'Basic {encoded}',
        }
      )
    print(json.loads(res.data.decode('utf-8'))['headers'])
    return Response({'status':True, 'payload':encoded},status.HTTP_200_OK)