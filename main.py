# Imports
from bs4 import BeautifulSoup as bs
import requests

url = 'https://ncov2019.live/data'

# request the website
r = requests.get(url)
# get the html from the request
page = r.text

# Create bs4 object and parse the html
soup = bs(page, 'html.parser')

# get world data table
table = soup.find('table', attrs={'id':'sortable_table_world'})

# get table rows
tableRows = table.findAll('tr')

# countries you want to see data on
countries = ['United States', 'Canada']

# loop to print out the Country Name, Confirmed Cases, New Cases, and Critical Cases
for row in tableRows[1:]:
    if row.find('td').text[38:].strip() in countries:
        columns = row.findAll('td')

        # prints Country Name
        print(columns[0].text[38:].strip())

        # formats and prints Confirmed Cases
        confirmedCases = columns[1].text.strip()
        formattedConfirmedCases = confirmedCases.split('+')[0].strip()
        print(f'Confirmed Cases: {formattedConfirmedCases}')

        # formats and prints New Cases
        newCases = columns[3].text.strip()
        formattedNewCases = newCases.split('+')[0].strip()
        print(f'New Cases: {formattedNewCases}')

        # formats and prints Critical Cases
        criticalCases = columns[5].text.strip()
        formattedCriticalCases = criticalCases.split('+')[0].strip()
        print(f'Critical Cases: {formattedCriticalCases}\n')
