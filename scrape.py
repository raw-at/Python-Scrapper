import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.yellowpages.com/search?search_terms=Coffee&geo_location_terms=Los+Angeles%2C+CA');

#to see html content  ---> r.content

soup = BeautifulSoup(r.content);  #r.content is html content
# print soup.prettify()  #make eaiser to read

#find all a tag
#a_tag = soup.find_all('a')

#for href
#for link in soup.find_all('a'):
    #print(link.text,link.get('href'))


g_data = soup.find_all('div',{'class':'info'})
for item in g_data:
    print(item.content)


    
