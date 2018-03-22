import requests
from random import randint

class HTTPRequest:
	list_headers = [
{"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"},
{"User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080214 Firefox/2.0.0.12"},
{"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19"},
{"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19"},
{"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0"},
{"User-Agent": "Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7552.EU"}]

	def request(self,url,timeout = 10):
		response = requests.get(url, headers=self.list_headers[randint(0, len(self.list_headers)-1)], timeout=timeout)
		if response.status_code != 200:
			 return self.request(url,timeout = 10)
		return response

	def get_soup(self,response):
		return BeautifulSoup(response.text, "lxml")



a=HTTPRequest()
response = a.request("http://www.esiee.fr/")
print(response.text)
