import urllib.parse
import urllib.request
para={
    'kw':"春运"
}
kw=urllib.parse.urlencode(para)
print(kw)
kw=urllib.parse.unquote(kw)
print(kw)

name="老王"
name=urllib.parse.quote(name)
print(name)
name= urllib.parse.unquote(name)
print(name)
name=urllib.request.quote(name)
print(name)
name=urllib.request.unquote(name)
print(name)