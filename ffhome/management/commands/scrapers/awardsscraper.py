from string import Template
from bs4 import BeautifulSoup
from ffhome.management.commands.base_scraper import *
import requests

class NetogramScraper(BaseScraper):
    url_template = Template('http://www.netogram.com/flims/display.cgi?starting_point=$start_index&search%3D1%26searchtype%3Dany%26searchtext%3D$festival%26column%3D3')
    searchWords = ['oscar',
                   'australian',
                   'bafta',
                   'cesar',
                   'berlin',
                   'globe',
                   'venice',
                   'cannes',
                   'sundance'
                  ]

    festivalNames = ['Academy Awards - OSCARS',
                     'Australian Film Institute Awards',
                     'BAFTA Film Awards',
                     'CESAR Film Awards',
                     'Berlin International Film Festival',
                     'Golden Globe Awards',
                     'Venice International Film Festival',
                     'Cannes International Film Festival',
                     'Sundance Film Festival',
                    ]

    def scrape(self):
        res = {}
        for (fn,sw) in zip(self.festivalNames,self.searchWords):
            res[fn] = self.get_awards_for_festival(sw)
        return res


    def get_awards_for_festival(self,name):
        awards = []
        i=1
        while(True):
            res = requests.get(self.url_template.substitute(start_index=i,festival=name))
            soup = BeautifulSoup(res.text,features='lxml')

            table = soup.find_all('table')[1] #Tag
            rows = table.find_all('tr') #ResultSet
            for r in rows[1:]:
                awards.append(self.parse_row(r))

            i += 20
            if len(rows) == 1:
                break
        return awards


    def parse_row(self,row):
        cols = row.find_all('td')
        return Film(cols[0].font.a.string.strip(),
                    cols[1].font.string.strip(),
                    cols[2].font.string.strip())
