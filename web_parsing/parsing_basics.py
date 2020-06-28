import urllib.request as request
import urllib.parse as parse
import re


url='https://www.w3schools.com/python/python_json.asp'
values={'s':'Python','submit':'JSON'}
data=parse.urlencode(values)
data=data.encode('utf-8')
req=request.Request(url,data)
resp=request.urlopen(req)

respData=resp.read()
paragraphs=re.findall(r'<p>(.*?)</p>',str(respData))
for eachP in paragraphs:
    print(eachP)