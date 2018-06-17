import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import csv

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl1 = 'http://www.moneycontrol.com/financials/'
serviceurl2 = "http://www.moneycontrol.com/india/stockpricequote/telecommunications-service/"

balanceSheet = ["Total Capital And Liabilities", "Total Assets", "Total Current Liabilities", "Total Current Assets",
                "Total Share Capital", "Inventories", "Trade Receivables", "Trade Payables"]

profitLoss = ["Profit/Loss For The Period", "Equity Share Dividend", "Profit/Loss Before Tax",
                "Depreciation And Amortisation Expenses", "Finance Costs", "Total Revenue", "Operating And Direct Expenses" ]

ratios = ["Current Ratio", "Quick Ratio", "Total Debt/Equity"]

inputFile = open('chemicals.csv', 'r')

outputFile = open('ChemicalData.csv', 'w', newline='')
outputFile.write('Company'+'|');
for item in balanceSheet:
    outputFile.write(item + '|')
for item in profitLoss:
    outputFile.write(item + '|')
for item in ratios:
    outputFile.write(item + '|')
outputFile.write('MARKET CAP(Rs CR)\n')


for company in inputFile :
    row = company.strip().split('|')
    companyName = row[0]
    urlName = row[1]
    urlAbbv = row[2]

    print(companyName, urlName, urlAbbv)
    outputFile.write(companyName+'|')

    '''************************ Balance Sheet Page *************************'''
    pagetype = '/balance-sheetVI/'
    url = serviceurl1 + urlName + pagetype + urlAbbv + "#" + urlAbbv
    #print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser',from_encoding="iso-8859-1")

    for attr in balanceSheet:
        attrValue = None
        a = soup.find('td', text=re.compile(attr))
        if a is not None:
            attrValue = a.findNext('td').contents[0]
        if attrValue is None:
            attrValue = 'NA'
        outputFile.write(str(attrValue)+'|')
        #print(attr, attrValue)

    '''************************ Profit and Loss Page *************************'''
    pagetype = '/profit-lossVI/'
    url = serviceurl1 + urlName + pagetype + urlAbbv + "#" + urlAbbv
    #print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser',from_encoding="iso-8859-1")

    for attr in profitLoss:
        attrValue = None
        a = soup.find('td', text=re.compile(attr))
        if a is not None:
            attrValue = a.findNext('td').contents[0]
        if attrValue is None:
            attrValue = 'NA'
        outputFile.write(str(attrValue)+'|')
        #print(attr, attrValue)

    '''************************ Ratio Page *************************'''
    pagetype = '/ratiosVI/'
    url = serviceurl1 + urlName + pagetype + urlAbbv + "#" + urlAbbv
    #print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser',from_encoding="iso-8859-1")

    for attr in ratios:
        attrValue = None
        a = soup.find('td',text=re.compile(attr))
        if a is not None:
            attrValue = a.findNext('td').contents[0]
        if attrValue is None:
            attrValue = 'NA'
        outputFile.write(str(attrValue)+'|')
        #print(attr, attrValue)

    '''****************** Stock Price Quote Page *************************'''
    url = serviceurl2 + urlName + "/" + urlAbbv
    #print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser',from_encoding="iso-8859-1")

    attr = "MARKET CAP"
    attrValue = None
    a = soup.find(text = re.compile(attr))
    if a is not None:
        attrValue = a.findNext('div').contents[0]
    if attrValue is None:
        attrValue = 'NA'
    outputFile.write(str(attrValue)+'\n')
    #print(attr, attrValue)

outputFile.close()
