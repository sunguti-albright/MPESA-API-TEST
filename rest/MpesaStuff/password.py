import base64
import json

def mpesa_password(paybill,passKey,m_time):
    encode= paybill+passKey+m_time

    
    #decoding the encoded string
    # data_to_encode = f'{paybill}:{passKey}:{m_time}'
    # encoded = base64.b64encode(data_to_encode.encode('utf-8'))
    # en=(encoded.decode('ascii'))
    # return en