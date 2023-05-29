import requests
from bs4 import BeautifulSoup
import csv

urls = ['https://www.x-rates.com/table/?from=USD&amount=1',
        'https://www.x-rates.com/table/?from=EUR&amount=1',
        'https://www.x-rates.com/table/?from=GBP&amount=1']
for url in urls:
    result = requests.get(url).text
    soup = BeautifulSoup(result, 'html.parser')

    #Opening a csv file to write the scraped info
    csv_file = open('Xrates_Daily_Rates.csv', 'a', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['Header', 'Date', 'Currency', 'Rate'])

    header = soup.find('span', class_='OutputHeader').text
    date = soup.find('span', class_='ratesTimestamp').text

    chart = soup.find('tbody')
    currency = chart.find_all('tr')

    for item in currency:
        currency_name = item.find('td').text
        rate = item.find('a').text

        csv_writer.writerow([header, date, currency_name, rate])

    csv_file.close()




