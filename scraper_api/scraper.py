import requests
from bs4 import BeautifulSoup
import pandas as pd


class Scraper():
    def __init__(self, url) -> None:
        self.url = url
        self.data = None
        self.week = None

    def scrape(self):

        html = requests.get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find_all('tr')

        h1 = None
        h2 = None
        d1 = {}
        run1 = []
        run2 = []
        header = rows[0]
        self.week = header.td.text
        for i, row in enumerate(rows[3:]):
            tds = [td.string for td in row if 'data-sheets-value' in td.attrs]
            vals = [td for td in tds if td != ' ']
            col1, col2 = vals[:3], vals[3:]

            if 'Average Weight' in col1 or 'Size' in col1:
                if h1 == None:
                    h1 = col1[0]
                else:
                    d1[h1] = run1
                    h1 = col1[0]
                    run1 = []
            elif col1 != [] and col2 != []:
                run1.append(col1)
            elif col2 == []:
                run2.append(col1)
            if 'Average Weight' in col2 or 'Size' in col2:
                if h2 == None:
                    h2 = col2[0]
                else:
                    d1[h2] = run2
                    h2 = col2[0]
                    run2 = []
            elif col2 != None:
                run2.append(col2)

        columns = ['item', 'avg weight/size', 'price/lb|unit']
        df_dict = {k: pd.DataFrame(v, columns=columns) for k, v in d1.items()}
        df = (pd.concat(df_dict)
                .reset_index(level=1, drop=True)
                .rename_axis('category')
                .reset_index()
                .dropna()
              )

        df = df.applymap(str)
        df['avg weight/size'] = df['avg weight/size'].map(weight_range_to_avg)
        df['price/lb|unit'] = df['price/lb|unit'].map(dollar_string_to_float)
        df['sale'] = df.item.str.contains('\*')
        self.data = df


def weight_range_to_avg(s: str):
    if '-' in s:
        vals = s.split('-')
        return sum([int(val) for val in vals])/len(vals)
    elif not s.isnumeric():
        return 0.0
    return float(s)


def dollar_string_to_float(s: str) -> float:
    if '$' in s:
        return float(s[1:])
    return float(s)


scraper = Scraper(
    'https://ag.purdue.edu/ansc/ButcherBlock/Pages/Meatlist.aspx')
scraper.scrape()
df = scraper.data
