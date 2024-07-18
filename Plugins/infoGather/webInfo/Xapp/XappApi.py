import subprocess
import json
import os
import threading

lock = threading.Lock()

def run_xapp(url):
    lock.acquire(True)
    # 构建命令行参数列表
    group = 'Plugins/infoGather/webInfo/Xapp/xray-plugins/group/hvv.list'
    xappFolder="./Plugins/infoGather/webInfo/Xapp"
    os.system('chmod +x {}/xapp'.format(xappFolder))
    cmd = ['./Plugins/infoGather/webInfo/Xapp/xapp', '-t', url, '-g', group]
    info = []
    
    # 调用命令行工具
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True, encoding='utf-8')
        #print("xapp 输出：")
        # 将输出解析为 JSON
        # print(result.stdout)
        data = "\n".join(result.stdout.split('\n')[8:])
        #print(data)
        data = json.loads(data)
        if data['value'].get('fingerprints'):
            for i in data['value']['fingerprints']:
                info.append(i['product']['name'])
            

# 打印结果
        #print(info)
        
    except subprocess.CalledProcessError as e:
        # print("xapp 运行出错：")
        # print(e.stderr)
        pass
    finally:
        lock.release()
    return info

# 使用示例
# group = 'xray-plugins\\group\\hvv.list'  # 请确保路径是正确的
# target_url = 'http://49.246.3.237/'  # 请确保 URL 是正确的
# run_xapp(target_url)