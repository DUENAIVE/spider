import urllib.request
import urllib.parse

kw=input("请输入关键字>>")
kw={
    'kw':kw
}
url="http://tieba.baidu.com/f?%s"%(urllib.parse.urlencode(kw))
headers={
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Mobile Safari/537.36"
}
'''发送消息'''
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)

html=response.read()
with open("./tieba.html","wb")as file:
    file.write(html)