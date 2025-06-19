# Tenda AC6V2.0_V15.03.06.23_multi firmware is vulnerable to Buffer Overflow via function "fromSetRouteStatic"

Firmware download website:

[AC6V2.0升级软件_腾达(Tenda)官方网站](https://www.tenda.com.cn/material/show/102855)

In the `fromSetRouteStatic` function, a user can craft a POST request to pass the **`list` parameter** to the backend. This `list` parameter is then **passed unvalidated** into the `save_staticroute_data` function. Inside `save_staticroute_data`, it's further processed by `sscanf(p, "%,,%,,%,,%s", dst_net, net_mask, net_gw, net_ifname);`, which writes the data directly to stack-allocated variables, leading to a **stack overflow**.

![image-20250619005545828](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250619005545828.png)

![image-20250619005628755](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250619005628755.png)

![image-20250619005856028](https://kingimg.oss-cn-hangzhou.aliyuncs.com/img/image-20250619005856028.png)