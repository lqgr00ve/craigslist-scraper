import BeautifulSoup
import md5
import re
import time
import urllib2

from config import settings

PRICE_REGEX = re.compile('\$([\d]+)')

all_entries = {}

def parse_entry(entry):
    ret = {}

    ret['id'] = md5.md5(str(entry)).hexdigest()

    link = entry.find('a')
    ret['link'] = link['href']

    hook = link.contents[0]
    ret['hook'] = hook

    price_g = PRICE_REGEX.search(hook)
    price_match = False
    if price_g:
        ret['price'] = int(price_g.group(1))
        if ret['price'] <= settings.max_rent:
            price_match = True
            

    neighborhood = entry.find('font').contents[0]
    ret['neighborhood'] = neighborhood

    neighborhood_match = False
    for n in settings.neighborhoods:
        if n in neighborhood:
            neighborhood_match = True

    ret['match'] = price_match and neighborhood_match

    return ret


def scrape():
    html = urllib2.urlopen(settings.url).read()
    soup = BeautifulSoup.BeautifulSoup(html)

    bq = soup.findAll('blockquote')[1]
    entries = bq.findAll('p')
    for entry in entries:
        parsed = parse_entry(entry)
        if parsed['id'] in all_entries:
            continue
        all_entries[parsed['id']] = parsed
        if parsed['match']:
            print parsed

if __name__ == '__main__':
    while True:
        scrape()
        time.sleep(settings.period)
