import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
result = requests.get(url).text
soup = BeautifulSoup(result, 'html.parser')

#Opening a csv file to write the scraped info
csv_file = open('IMDBs_Top_250_TV_Shows.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Poster', 'Title', 'Year', 'Stars'])

chart = soup.find('tbody', class_='lister-list')
shows = chart.find_all('tr')

for show in shows:
    poster = show.find('td', class_='posterColumn')
    poster_2 = poster.find('img').attrs['src']
    rank_name_year = show.find('td', class_='titleColumn')
    title = rank_name_year.find('a').text
    year = rank_name_year.find('span').text
    stars = show.find('td', class_='ratingColumn imdbRating').text
    stars_formatted = stars.strip()

    csv_writer.writerow([poster_2, title, year, stars_formatted])

csv_file.close()




