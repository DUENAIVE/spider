import urllib.request
# url作为Request()参数构造并返回一个Request对象
# request=urllib.request.Request('http://www.baidu.com')
request=urllib.request.Request("https://www.sina.com.cn/")
# Request对象作为urlopen的参数,发送给服务器并接受响应
response=urllib.request.urlopen(request)
# 读取响应回来的数据
html=response.read()
with open('./sina.html','wb') as file:
    file.write(html)
