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

**Docker**
You need BuildKit enabled, can do so with `export DOCKER_BUILDKIT=1`
```bash
docker build -t butcher_block .
docker run -d -p 8501:8501 butcher_block
```
**python**
with pyenv
```
pyenv virtualenv 3.8.10 butcher-block-3.8.10
pyenv activate butcher-block-3.8.10
streamlit run src/dash.py
```
