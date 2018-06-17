import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import csv


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

auto = ["auto-2-3-wheelers", "auto-cars-jeeps", "auto-lcvs-hcvs", "auto-tractors", "auto-ancillaries"]
telecom = ["telecommunications-service", "telecommunications-equipment"]
steel = ["steel-cr-hr-strips", "steel-gp-gc-sheets", "steel-large", "steel-medium-small", "steel-pig-iron", "steel-rolling", "steel-sponge-iron", "steel-tubes-pipes"]
chemicals = ["chemicals"]

serviceurl = 'http://www.moneycontrol.com/stocks/marketinfo/marketcap/bse/'

for item in chemicals:
    url = serviceurl+item+'.html'
    print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())

    companyRows = soup.find_all("td", class_="brdrgtgry")
    #print(companyRows)
    s = None
    with open('chemicals.csv', 'a', newline='') as out:
        spamwriter = csv.writer(out, delimiter='|')
        for company in companyRows:
            atag = company.find('a')
            if atag != None:
                fullName = atag.get_text()
                s = atag["href"].split("/")
                urlName = s[4]
                urlAbbv = s[5]

                spamwriter.writerow([fullName, urlName, urlAbbv])
                print(fullName +": "+ urlName + " " + urlAbbv)
            s = None
    out.close()
