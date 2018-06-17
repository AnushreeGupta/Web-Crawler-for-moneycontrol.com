# Web Crawler for moneycontrol.com


Built a web crawler to fetch financial data for companies from Money Control website. The HTML parsing is done using Beautiful Soup. The crawler performs the required tasks in two steps.

1. Fetch the company list ranging across four sectors - Auto, Telecom, Steel and Chemicals (http://www.moneycontrol.com/stocks/marketinfo/marketcap/bse/). This list is fetched in a csv file which also captures the short names for the company which will be used to recreate URLs for each company and get the desired data. 

2. In second step we recreate URLs for all the company details we collected in Step 1 and crawl data required for all the required fields. The required fields are spread across the below four pages as listed below. This data is saved in csv files as well.
    1. Balance Sheet Page
    2. Profit and Loss Page
    3. Ratio Page
    4. Stock Price Quote Page
