import urllib.request
head={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
request=urllib.request.Request("https://www.autohome.com.cn",headers=head)
print(request.headers)
response=urllib.request.urlopen(url=request)
html=response.read()
with open('./autohome.html','wb')as file:
    file.write(html)