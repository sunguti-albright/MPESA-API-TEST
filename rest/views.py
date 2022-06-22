
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest.MpesaStuff.token import mpesa_token
from .conf import *
from rest.MpesaStuff import *

import json
import base64
import urllib3
import pybase64

http = urllib3.PoolManager()    

# Create your views here.
@api_view(['GET'])
def get_mpesa_auth(request):
    # print(request.method)
    # #encoding the consumer key and consumer secret
    # data_to_encode = f'{conf["CONSUMER_KEY"]}:{conf["CONSUMER_SECRET"]}'
    # print(data_to_encode)
    # encoded = base64.b64encode(data_to_encode.encode('utf-8'))
    # en=(encoded.decode('ascii'))

    # res=http.request(
    #     method='GET',
    #     url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
    #     headers={
    #         'Authorization': f'Basic {en}',
    #     }
    #   )
    # data= json.loads(res.data.decode('utf-8'))
    # print(data)
    data=mpesa_token()
    # return Response({'status':True, 'payload':data},status.HTTP_200_OK)

@api_view(['POST'])
def stkPush(request):
  m_time= mpesa_time()
  p_key='bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
  m_pass=mpesa_password('174379',p_key,m_time)
  token = mpesa_token()
  res=stk_push(254705289881,1,m_pass,m_time,token['access_token'])
  
  return Response({'status':True, 'payload':res},status.HTTP_200_OK)
    