import requests

class HTTPRequest:
	headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"}

	def request(self,url,timeout = 10):
		response = requests.get(url, headers=self.headers, timeout=timeout)
		if response.status_code != 200:
			 return self.request(url,timeout = 10)
		return response

a=HTTPRequest()
response = a.request("http://www.esiee.fr/")
print(response.text)
