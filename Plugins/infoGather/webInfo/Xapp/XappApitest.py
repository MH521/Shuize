import subprocess
import json
import os

def run_xapp(grouip,url):
    # 构建命令行参数列表
    # group = 'Plugins/infoGather/webInfo/Xapp/xray-plugins/group/hvv.list'
    # xappFolder="./Plugins/infoGather/webInfo/Xapp"
    # os.system('chmod +x {}/xapp'.format(xappFolder))
    cmd = ['xapp.exe', '-t', url, '-g', group]
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
        
        for i in data['value']['fingerprints']:
            info.append(i['product']['name'])
            

# 打印结果
        print(info)
        
    except subprocess.CalledProcessError as e:
        # print("xapp 运行出错：")
        # print(e.stderr)
        pass
    return info

# 使用示例
group = 'xray-plugins\\group\\hvv.list'  # 请确保路径是正确的
target_url = 'http://sso.binjiang.com.cn:7003/'  # 请确保 URL 是正确的
run_xapp(group,target_url)