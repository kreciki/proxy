#Python3.7.6 Win7 运行通过 (2021.7.11)
import os #导入os模块进行文件操作
import urllib.request
import urllib.error
#from urllib import request,error

file_address='f:\p1.txt' #设置IP地址文件路径
with open(file_address,'r') as f1:  # 打开文件 with open('f:\p1.txt','r') as f1:
    ip_address=f1.read().splitlines() #去掉换行符后形成一个list列表文件
print("待验证的IP列表",ip_address)

b=list(set(ip_address))  #通过set()去除重复IP，再通过list()转换回列表
print("="*60)
print("共计："+str(len(ip_address))+"个，"+"去除重复后，共计："+str(len(b))+"个")
print("IP地址文件导入路径",file_address)

niming_txt='f:\ip_3_niming.txt'# 匿名代理IP验证成功后的写入路径
url="http://httpbin.org/ip" #url = 'http://myip.ipip.net'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
req= urllib.request.Request(url=url,headers=headers)# 构造请求，加入headers
response=urllib.request.urlopen(req)                # 用urlopen()发送构造的请求
local_ip=response.read().decode('utf-8').split('\"')[3]#对返回字符串进行分割形成列表，再根据索引值[3]提取本机ip地址
print("当前本机公网IP（未设置代理）：",local_ip)
print("="*60)
print("开始进行代理IP验证......")
count=0      # 计数器初始设置

for x in b:  # 循环遍历IP地址列表
    proxy = {'http': x}           #代理服务器
    http_handler=urllib.request.HTTPHandler#(debuglevel=1)
    # 2.创建ProxyHandler
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = urllib.request.build_opener(proxy_handler,http_handler)
    
    # 4.安装Opener
    urllib.request.install_opener(opener)
    request = urllib.request.Request(url,headers=headers)

    # 调用自定义opener对象的open()方法，发送request请求
        
    try:
        rsp = opener.open(request,timeout=4) #发送请求
        html = rsp.read().decode() #接收响应，并解码
        
        if local_ip in html: ## 检测本机IP是否出现在httpbin.org/ip页面，如果检测到，说明是透明代理
            with open('f:\ip_3_touming.txt',"a",encoding='utf-8') as proxy_ip:
                proxy_ip.write('%s\n' % str(proxy['http']))#写入该代理IP 
            print("*"*60)
            print("验证成功（透明）:",proxy['http'],html)
            print("*"*60)
        else:
            
            with open(niming_txt,"a",encoding='utf-8') as proxy_ip: #"a"追加方式写入
                proxy_ip.write('%s\n' % str(proxy['http']))#写入该代理IP
            count=count+1 # 计数器
            print("*"*60)
            print("验证成功（匿明）:",x,html)
            print("*"*60)
            
    except urllib.error.URLError as e: # 如果是from urllib import request,error不用写urllib
        print("失败",proxy['http'],"错误",e)
    except urllib.error.HTTPError as e:
        print("失败",proxy['http'],"错误",e)
    except Exception as e:
        print("失败",proxy['http'],"错误",e)
print("="*60)        
print("共验证成功匿名代理IP："+str(count)+"个!") #字符串可以通过加号拼接
print("文件保存位置",niming_txt)


#https://www.proxyscrape.com（推荐，可直接下载代理服务器数据）
#b=input("请输入ip文本：").split(',')
#http://free-proxy.cz/en/ Free proxy servers list
#https://free-proxy-list.net/
#https://www.hide-my-ip.com/proxylist.shtml
#https://geonode.com/free-proxy-list
#https://freevpn4you.net/free-proxy.php
#https://www.javatpoint.com/proxy-server-list
#https://hidemy.name/en/proxy-list/
#https://spys.one/en/ 俄语
#https://hideip.me/en/proxy/httplist
#https://advanced.name/freeproxy?ddexp4attempt=1
#https://www.kuaidaili.com/free/intr/
#【ip查询网址】
#http://ip.42.pl/（显示http请求报文）
#http://ip.42.pl/raw（纯文本）
#http://myip.ipip.net（国内，纯文本）
#http://www.whatismyip.com.tw/
#http://httpbin.org/ip
#测试IP：test IP 139.224.18.116:80,139.196.205.67:8080,139.224.45.199:8080,106.14.245.34:8080,139.224.211.123:8080,139.196.219.86:8080,139.196.152.83:8080,139.196.112.180:8080,139.196.155.217:8080,139.224.211.9:8080,139.196.152.221:8080,139.196.154.130:8080,106.14.41.224:8080,47.102.47.126:8080,114.215.198.156:80,106.15.8.56:8080,106.14.41.100:8080,106.14.198.6:8080,106.14.43.27:8080,106.14.249.30:8080,106.14.42.155:8080,106.14.250.220:8080,139.224.45.151:8080,101.132.189.87:9090,106.14.248.171:8080,139.224.115.161:8080,139.224.44.82:8080,106.14.249.30:8080,106.14.40.108:8080,139.224.210.204:8080,101.132.189.87:9090,121.41.208.160:3128,106.14.245.34:8080,223.241.77.24:3256,124.205.153.19:80,119.84.112.137:80,106.45.105.221:3256,203.91.121.212:3128,115.233.221.139:3128,112.245.17.202:8080,139.9.25.69:3128,218.86.87.171:31661,60.191.11.249:3128,58.212.41.239:3256,223.241.77.8:3256,121.37.189.26:8118,117.64.237.66:9999,180.97.61.80:80,180.97.81.38:80,58.220.95.107:80,58.220.95.78:9401,60.191.11.249:3128,60.191.11.241:3128,60.191.11.249:3128,124.74.247.82:80,27.109.116.119:23500,122.176.65.143:31021,62.205.169.74:53281,219.131.214.150:4216,14.18.109.42:8081,173.46.67.172:58517,158.69.25.178:32769,200.35.56.161:35945,181.196.254.202:53281,51.222.21.95:32768,207.157.25.44:80,202.77.120.38:57965,183.88.213.85:8080,103.87.206.249:48792,61.72.254.69:80,74.143.245.221:80,140.227.71.165:6000,122.15.211.124:80,198.50.163.192:3129,118.117.188.156:3256,14.97.2.106:80,129.205.161.242:31075,192.140.42.81:47277,68.183.89.13:80,119.28.17.168:8085,87.237.234.187:3128,45.174.70.18:53281,92.204.129.161:80,186.167.33.244:42550,119.84.112.137:80,115.233.221.139:3128,47.107.128.69:888,121.41.208.160:3128,182.140.244.163:8118,47.98.170.216:8080,159.69.66.224:8080,203.91.121.212:3128,47.106.211.65:3228,159.69.66.224:8080,203.91.121.212:3128,59.37.18.243:3128,47.106.211.65:3228,218.75.158.153:3128

#文件操作：读取f:\p.txt文件，写入 ip_address 列表
#ip_address = []
#with open('f:\ip_1.txt', 'r') as f1:
#    for ip in f1.readlines():#逐行读取txt每行，末尾会带换行符\n
#        if ip != None:
#            # 使用strip()函数去掉换行符\n，再用append添加入列表ip_address
#            ip_address.append(ip.strip("\n"))

