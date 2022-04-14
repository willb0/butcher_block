from fastapi import FastAPI
from scraper import Scraper
from typing import Optional
import json

api = FastAPI()
scraper = Scraper('https://ag.purdue.edu/ansc/ButcherBlock/Pages/Meatlist.aspx')

@api.get('/')
def home():
    return {'This is the home page. hit /scrape to scrape the butcher block site and /results to check the results'}
@api.get('/scrape')
def scrape():
    try:
        scraper.scrape()
    except Exception as e:
        return {'Error':e}

    return {'Scrape':'Successful'}
@api.get('/results')
def results():
    if scraper.data is None:
        return {'Havent scraped yet':'Hit the /scrape endpoint'}
    else:
        return json.loads(scraper.data.to_json())