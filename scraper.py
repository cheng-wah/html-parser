from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import datetime


my_url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=naruto+pin&_in_kw=1&_ex_kw=&_sacat=0&LH_Sold=1&_udlo=&_udhi=&_samilow=&_samihi=&_sargn=-1%26saslc%3D1&_salic=1&_sop=12&_dmd=1&_ipg=200&LH_Complete=1&_fosrp=1'

uClinet = uReq(my_url)
page_html = uClinet.read()
page_soup = soup(page_html, 'html.parser')

container = page_soup.findAll('li',{'class':"sresult lvresult clearfix li"})


filename = 'product.csv'
f = open(filename, 'w')
headers = 'image, title, sold_price, shipping, sales_time\n'
f.write(headers)

for i in range(len(container)):
    img = container[i].div.div.a.img['src']
    title = container[i].h3.text.strip()
    sold_price = container[i].findAll('span',{'class':'bold bidsold'})[0].text.strip()
    ship = container[i].findAll('span',{'class':'ship'})[0].text.strip()
    sales_time_temp = container[i].findAll('span',{'class':'tme'})[0].text.strip()
    sales_time = datetime.datetime.strptime(sales_time_temp, '%b-%d %H:%M').strftime('%d/%m')
 
    f.write(img + ',' + title.replace(',','|') + ',' + sold_price + ',' + ship + ',' + sales_time + '\n')

f.close()