import urllib.request
url='https://movie.douban.com/top250'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.7 Safari/537.36'
}
req=urllib.request.Request(url=url,headers=header)
response=urllib.request.urlopen(req)
html=response.read().decode('utf-8')
print(html)