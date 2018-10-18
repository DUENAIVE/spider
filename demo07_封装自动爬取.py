import urllib.request
import urllib.parse

def spider_tieba(url, begin, end, kw):
    '''
    爬虫类
    :param url:
    :param begin:
    :param end:
    :param kw:
    :return:
    '''
    for i in range(begin, end+1):
        pn = (i - 1) * 50
        paras = {
            'kw': kw,
            'pn': pn
        }
        para=urllib.parse.urlencode(paras)
        full_url = url + para
        file_name = "./tieba-%s.html" % i
        html=loadpage(full_url,para)
        write(html, file_name)

def loadpage(full_url,para):
    '''
    加载图片类
    :param url:
    :return:
    '''
    headers={
        "Referer": "http://tieba.baidu.com/f?"+para,
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Mobile Safari/537.36"
    }
    request = urllib.request.Request(full_url,headers=headers)
    response = urllib.request.urlopen(request)
    return response.read()

def write(html,file_name):
    '''
    写到本地
    :param html:
    :param file_name:
    :return:
    '''
    print("--------begin---------")
    with open(file_name, "wb")as file:
        file.write(html)
        print("--------end---------")


# 调用
if __name__ == '__main__':
    url="http://tieba.baidu.com/f?"
    kw=input("请输入关键字>>")
    begin=int(input("开始页面>>"))
    end=int(input("结束页面>>"))
    spider_tieba(url,begin,end,kw)