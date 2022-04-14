import streamlit as st
import pandas as pd
import requests

requests.get('http://api:80/scrape')
res = requests.get('http://api:80/results').json()
if len(res) < 2:
    st.write('Error in scraping')
    st.write
else:
    df = pd.DataFrame.from_dict(res)
    st.title('Purdue butcher block weekly items')
    st.header('Items on sale this week:')
    sales = df[df.sale==True][['item','avg weight/size','price/lb|unit']]
    for sale in sales.iterrows():
        item, weight, price = sale[1]
        st.subheader(f'{weight} lbs of {item} for ${weight * price}')


    categories = list(df.category.unique())
    categories.insert(0,'All')
    sort = ['Weight','Price per lb']
    sort.insert(0,'None')

    choice = st.selectbox('Pick a category of products',categories,index=0)
    sort_choice = st.selectbox('Sort by weight or price',sort)
    by_choice = st.checkbox('Ascending',value=False)


    results = df[['category','item','avg weight/size','price/lb|unit']].copy()

    if sort_choice != 'None':
        if sort_choice == 'Weight':
            results.sort_values(by='avg weight/size',ascending=by_choice,inplace=True)
        else:
            results.sort_values(by='price/lb|unit',ascending=by_choice,inplace=True)
    if choice != 'All':
        results = results[results.category == choice]
    st.table(results[['item','avg weight/size','price/lb|unit']])








