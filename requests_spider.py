import requests
from lxml import html

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Origin': 'http://vip.biancheng.net',
	'Host': 'vip.biancheng.net',
	'Referer': 'http://vip.biancheng.net',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
	'Upgrade-Insecure-Requests': '1',
}


session_requests = requests.session()

login_url = "http://vip.biancheng.net/login.php"
result = session_requests.get(login_url)

# tree = html.fromstring(result.text)
# authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
# username=niejn&password=cxf8922470&submit=%E7%99%BB%C2%A0%C2%A0%C2%A0%C2%A0%E5%BD%95
payload = {
	"username": "niejn",
	"password": "cxf8922470",
	"submit": "%E7%99%BB%C2%A0%C2%A0%C2%A0%C2%A0%E5%BD%95"
}
result = session_requests.post(
	login_url,
	data = payload,
	headers = headers
)

url = 'http://c.biancheng.net/cpp/biancheng/view/2995.html'
result = session_requests.get(
	url,
	headers = dict(referer = url)
)
result.encoding = 'gbk'
print(result.text)

# result.ok # Will tell us if the last request was ok
# result.status_code # Will give us the status from the last request
