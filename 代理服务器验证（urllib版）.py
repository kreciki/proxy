import os #导入os模块进行文件操作
import urllib.request
import urllib.error
from urllib import request,error

#文件操作：读取f:\p.txt文件，写入 ip_address 列表
#ip_address = []
#with open('f:\ip_1.txt', 'r') as f1:
#    for ip in f1.readlines():#逐行读取txt每行，末尾会带换行符\n
#        if ip != None:
#            # 使用strip()函数去掉换行符\n，再用append添加入列表ip_address
#            ip_address.append(ip.strip("\n"))

file_address='f:\p1.txt' #设置IP地址文件路径
with open(file_address,'r') as f1:  # 打开文件 with open('f:\p1.txt','r') as f1:
    ip_address=f1.read().splitlines() #去掉换行符后形成一个list列表文件
print("待验证的IP列表",ip_address)
print("共计",len(ip_address),"个")
print("IP地址文件路径",file_address)
print("="*40)
print("开始进行IP验证...")

if __name__ == '__main__':
    #url='http://ip.42.pl/raw'
    url="http://httpbin.org/ip"
    #url = 'http://myip.ipip.net'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    # 使用代理的步骤
  
    #b=input("请输入ip文本：").split(',')
    b=ip_address
for x in b:  # 循环遍历IP地址列表
    proxy = {'http': x} #代理服务器
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
        rsp = opener.open(request,timeout=4)
        html = rsp.read().decode() #接收
        # 检测httpbin.org/ip能否识别本机IP
        if "117.152.78.81" in html:
            with open('f:\ip_2_touming.txt',"a",encoding='utf-8') as proxy_ip:
                proxy_ip.write('%s\n' % str(proxy['http']))#写入该代理IP 
            print("*"*60)
            print("验证成功（透明）:",x,proxy['http'],html)
            print("*"*60)
        else:
            with open('f:\ip_2_niming.txt',"a",encoding='utf-8') as proxy_ip:
                proxy_ip.write('%s\n' % str(proxy['http']))#写入该代理IP 
            print("*"*60)
            print("验证成功（匿明）:",x,proxy['http'],html)
            print("*"*60)
            
    except error.URLError as e:
        print("失败",proxy['http'],"错误",e)
    except error.HTTPError as e:
        print("失败",proxy['http'],"错误",e)
    except Exception as e:
        print("失败",proxy['http'],"错误",e)

