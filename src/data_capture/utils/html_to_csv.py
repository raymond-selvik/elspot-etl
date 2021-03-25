from bs4 import BeautifulSoup
import sys
import csv

soup = BeautifulSoup(open("daily.xls"))

header = [cell.get_text().strip().encode('ascii', 'ignore') for cell in soup.find('thead').find_all('tr')[-1].find_all('td')]

formated_headers = []

for name in header:
    name = str(name)
    name = name[2:-1]
    formated_headers.append(name)

header = ['Date'] + formated_headers[1:]

data = [[cell.get_text().strip().replace(',', '.') for cell in row.find_all('td')]
      for row in soup.find('tbody').find_all('tr')]

with open('out.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(header)

    for row in data:
        write.writerow(row)