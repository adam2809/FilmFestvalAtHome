from string import Template
from bs4 import BeautifulSoup
import requests

url_template = Template('http://www.netogram.com/flims/display.cgi?starting_point=$start_index&search%3D1%26searchtype%3Dany%26searchtext%3D$festival%26column%3D3')

festivals = ['oscar',
             # 'bafta',
             # 'cesar',
             # 'berlin',
             # 'venice',
             # 'cannes',
             # 'australian',
             # 'sundance',
             # 'globe',
            ]

def get_awards_for_festival(name):
    i=1
    print(name+'         <<<')
    while(True):
        res = requests.get(url_template.substitute(start_index=i,festival=name))
        soup = BeautifulSoup(res.text,features='lxml')
        table = soup.find_all('table')[1]
        rows = table.find_all('tr')
        print(rows)
        break

if __name__ == '__main__':
    for fest in festivals:
        get_awards_for_festival(fest)
