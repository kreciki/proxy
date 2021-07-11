#python3.7.6 Win7
import os
import requests
#import requests.exceptions

    # 打开文件，分割、去重
with open("f:\ip_1.txt","r") as f: #用with open,可以不用.close()关闭
    ip_list=f.read().split("\n") #效果和f.read().splitlines()一样，生成一个列表
    #ip_list=f.read().splitlines() 另外一种写法
print(ip_list)
print("共计",len(ip_list),"个IP") #列表里可能有重复
ip_list_remove=list(set(ip_list)) #先用set()转成集合去掉重复，再转回列表
print("去重后共计",len(ip_list_remove),"个IP")


niming_txt='f:/NM_ip.txt'#验证通过的IP保存地址
url="http://www.httpbin.org/ip"
headers={"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
resp_origin=requests.get(url,headers=headers,timeout=5)#无代理访问，获取本机公网IP地址
resp_origin.text # .text获取返回网页，是字符串'{\n  "origin": "117.152.78.21"\n}\n'
origin_ip=resp_origin.text.split("\"")[3]#按"进行分割，生成列表，再根据列表索引值提取IP
print("本机当前公网IP:",origin_ip)
print("开始验证......","\n","*"*60)

count_1=0                # 透明代理计数器
count_2=0                # 匿名代理计数器
num=len(ip_list_remove)  # 剩余数量计数器

for i in ip_list_remove:
    ip_port=i     #ip_port，IP地址和端口，循环遍历IP
    url="http://www.httpbin.org/ip"
    headers={"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    proxies={"http":"http://{}".format(ip_port)} # 代理服务器
    
    try:
        resp=requests.get(url,headers=headers,proxies=proxies,timeout=5)#发送
        resp.raise_for_status()# .raise_for_status()方法，只要判断不是200就抛出异常
        
        if origin_ip in resp.text:  #检测返回网页是否含有origin_ip"117.152.78.21"
            with open('f:/TM_ip.txt','a') as f: # 搞不懂为什么不能写f:\
                f=f.write('{}\n'.format(ip_port)) # 写入IP并加一个换行符，换行
                count_1=count_1+1
                print("-"*30)
                print(resp.text)
                print("验证成功(透明）",count_1,"个IP") #计数器
                print("-"*30)
        else:            
            with open(niming_txt,'a') as f: # 搞不懂为什么不能写f:\
                f=f.write('%s\n'% ip_port) # 使用%进行格式化，写入一个IP并换行
                count_2=count_2+1          #f.write(str)括号必须为字符串str
                print("-"*30)
                print(resp.text)
                print("验证成功(匿名）",count_2,"个IP") #计数器
                print("-"*30)
    except Exception as e:        # requests.exceptions as e: 好像也可以
        print("[Error]",ip_port)  #print("[Error]",e) #失败的IP
        print("出现异常","类型为：{}","内容为:{}".format(type(e)))
    num=num-1
    print("剩余",num,"个")

print("="*60)        
print("共验证成功匿名代理IP："+str(count_2)+"个!") #字符串可以通过加号拼接
print("文件保存位置",niming_txt)

#其他参考写法   
#except requests.ConnectTimeout as e :
#    print(e)
#except requests.exceptions.ProxyError as e:
#    print(e)
#except requests.ConnectionError as e:
#    print(e)
#print("出现异常","类型为：{}","内容为:{}".format(type(e),str(e)))
