import re
import csv
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup


def scrape_emails(url):
	'''Scrapes email from a given URL and return list of all the e-mails found on that webpage'''

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req), 'html.parser')
    email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', re.VERBOSE)
    emails = email_regex.findall(soup.prettify())
    emails += email_regex.findall(soup.text)

    return list(set(emails))


def read_write(path):
	'''Reads a list of URLs from a given .csv file, and saves all the e-mails found on that site to a new .csv file'''

    with open(path, newline='') as input_file:
        with open('.\\output.csv', mode='w', newline='') as output_file:
            spamreader = csv.reader(input_file)
            spamwriter = csv.writer(output_file)

            for row in spamreader:
                email_list = scrape_emails(row[0])
                spamwriter.writerow([row[0]] + email_list)


read_write(input('Enter the full Path to the input .csv file: '))
print('Done!\nRegards from SkullTech.')
