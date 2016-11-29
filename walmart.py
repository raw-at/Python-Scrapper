import urllib.request
import html
import bs4 as bs

url = "https://www.walmart.com/cp/1078664"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
response1 = response.read().decode('utf-8')

data = html.unescape(response1)
soup = bs.BeautifulSoup(data,'html.parser')
div_data = soup.find_all('script')
script_dict = div_data[19].get_text()
print(script_dict)