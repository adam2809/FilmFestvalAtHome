from string import Template
from bs4 import BeautifulSoup
import requests

url_template = Template('http://www.netogram.com/flims/display.cgi?starting_point=$start_index&search%3D1%26searchtype%3Dany%26searchtext%3D$festival%26column%3D3')

festivals = ['oscar',
             'bafta',
             'cesar',
             'berlin',
             'venice',
             'cannes',
             'australian',
             'sundance',
             'globe',
            ]

class Film:
    def __init__(self,name,award,year):
        self.name = name
        self.award = award
        self.year = year

    def __str__(self):
        return f'name={self.name}    award={self.award}   year={self.year}'


def parse_row(row):
    cols = row.find_all('td')
    return Film(cols[0].font.a.string.strip(),
                cols[1].font.string.strip(),
                cols[2].font.string.strip())


def get_awards_for_festival(name):
    awards = []
    i=1
    print(name+'         <<<')
    while(True):
        res = requests.get(url_template.substitute(start_index=i,festival=name))
        soup = BeautifulSoup(res.text,features='lxml')

        table = soup.find_all('table')[1] #Tag
        rows = table.find_all('tr') #ResultSet
        for r in rows[1:]:
            awards.append(parse_row(r))
            print(awards[-1])

        i += 20
        if len(rows) == 1:
            break
    return awards

def get_awards_for_all_festivals():
    res = {}
    for fest in festivals:
        res[fest] = get_awards_for_festival(fest)
    return res


if __name__ == '__main__':
    get_awards_for_all_festivals()
