import urllib.request
import urllib.parse
kw=input("关键字>>")
begin=int(input("开始页面>>"))
end=int(input("结束界面>>"))

for i in range(begin,end+1):
    pn=(i-1)*50

    para={
        "kw":kw,
        "pn":pn
    }
    url="http://tieba.baidu.com/f?%s"%(urllib.parse.urlencode(para))

    request=urllib.request.Request(url=url)
    response=urllib.request.urlopen(request)

    html=response.read()


    print("--------begin---------")
    with open("./tieba-%s.html"%i,"wb")as file:
        file.write(html)
        print("--------end---------")