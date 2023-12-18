from urllib.request import urlopen, Request
url = 'https://google.com'
request = Request(url)
response = urlopen(request)
response = response.read()
for x in response:
    print(x)
