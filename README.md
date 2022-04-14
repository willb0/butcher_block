# Purdue butcher block scraper

This repo is my ongoing project to build a system that texts me when my University butcher has specific meats in stock (chuck eyes)

### Progress

I think it will be a multiple step process:

- [x] Scrape the butcher block site into some python data structure, and build filtering frontend in Streamlit.
- [ ] Store the data in a relational database (postgres?) 
- [ ] Build a system to periodically scrape the website and check for updates, can do this by checking first row on the site for a date update.
- [ ] Add a functionality on frontend to input a phone number and a request for a product. Create new database with requests.
- [ ] On website update, check request database to see if any products are in it. If so, send texts to all requesters

### Setup

**Docker-compose**
You need BuildKit enabled, can do so with `export DOCKER_BUILDKIT=1`
```bash
docker-compose build
docker-compose up
```
**python**
with pyenv and pyenv-virtualenv
```
pyenv virtualenv 3.8.10 butcher-block-3.8.10
pyenv activate butcher-block-3.8.10
pip install -r scraper_api/requirements.txt frontend/requirements.txt
uvicorn scraper_api.main:api --host 0.0.0.0 --port 80 && streamlit run frontend/dash.py --server.port=81
```
