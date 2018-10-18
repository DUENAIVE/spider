# 处理URL
import urllib.parse
kw=input('请输入关键字>>')
kw={
    "kw":kw
}

url="http://tieba.baidu.com/f?%s"%(urllib.parse.urlencode(kw))
print(url)