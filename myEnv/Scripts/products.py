from bs4 import BeautifulSoup
from requests.sessions import HTTPAdapter
import urllib3
import requests
# using time module
import time

# ts stores the time in seconds
ts = time.time()

class Scrapper:
	def __init__(urlObject, url):
		urlObject.url = url
	def showList(abc):
		html_page = requests.get(abc.url)
		soup = BeautifulSoup(html_page.content, "html.parser")
		file = open('products\productlisting'+str(ts)+'.txt', 'w')
		# Text Content Body
		#print("Body: Product Lisiting ")
		for textcontent in soup.find_all(["li"], class_="s-item"):
			#print(textcontent.text)
			file.write(textcontent.find(["h3"], class_="s-item__title").text)
			file.write("\n")
		file.close()

siteToScrap = Scrapper("https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&_pgn=1")
siteToScrap.showList()
