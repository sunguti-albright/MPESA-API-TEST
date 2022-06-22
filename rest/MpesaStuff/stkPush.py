import urllib3
import json
import base64
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
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X" 
}


def stk_push(phone,amount,Password, Timestamp,token):
    # conf['Password']=Password
    # conf['Timestamp']=Timestamp
    # conf['Amount']=amount
    # conf['PartyA']= phone
    # conf['PhoneNumber']= phone
    payload=json.dumps(conf).encode('utf-8')
    url= "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    print(payload)
    res=http.request(method='POST',
                url=url,
                body=payload,
                headers={'Authorization':f'Bearer {token}'}
                )
   
    data=json.loads(res.data.decode('utf-8'))
   
    return data

