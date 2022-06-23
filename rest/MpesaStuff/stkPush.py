import urllib3
import json
import base64
import requests
http = urllib3.PoolManager()

conf={
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIwNjIyMjAzNzA0",
    "Timestamp": "20220622203704",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254799735661,
    "PartyB": 174379,
    "PhoneNumber": 254799735661,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "ParkIt ",
    "TransactionDesc": "Payment of Parking Slot" 
}


def stk_push(phone,amount,Password, Timestamp,token):
    # conf['Password']=Password
    # conf['Timestamp']=Timestamp
    # conf['Amount']=amount
    # conf['PartyA']= phone
    # conf['PhoneNumber']= phone+
    # payload=json.dumps(conf)
    url= "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    
    res=requests.post(
                url=url,
                json=conf,
                headers={'Authorization':f'Bearer {token}'}
                )
   
    data=res.json()
   
    return data

