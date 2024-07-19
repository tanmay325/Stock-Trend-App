import streamlit as st
import requests
import pandas as pd
from streamlit.hashing import _CodeHasher

# Define API endpoint and parameters
endpoint = 'https://finnhub.io/api/v1/news'
params = {'category': 'general', 'symbol': 'AAPL', 'token': 'cgos5p9r01qlmgv25aigcgos5p9r01qlmgv25aj0'}

def get_stock_news(company):
    # Update API parameters with selected company symbol
    params['symbol'] = company

    # Make API request and parse response as JSON
    response = requests.get(endpoint, params=params)
    news_data = response.json()

    # Create a dataframe to store news data
    news_df = pd.DataFrame(news_data)

    # Select relevant columns and rename them
    news_df = news_df[['headline', 'summary', 'url']]
    news_df.columns = ['Headline', 'Summary', 'URL']

    return news_df

def news_tab():
    st.title('📰 Stock News')

    # Get company symbol from user input
    company = st.sidebar.text_input('Enter company symbol (e.g. AAPL):')

    if not company:
        st.warning('Please enter a company symbol')
        return

    st.write(f'Showing news for {company}')

    # Get stock news for the selected company
    try:
        news_df = get_stock_news(company)
        news_df.index = news_df.index + 1
        # Set table background color to light gray and font color to black
        styles = [
            dict(selector='table', props=[('background-color', '#f7f7f7'), ('color', 'black')])
        ]
        st.set_table_styles(styles)
        st.table(news_df.head(10))
    except:
        st.error('Error fetching news data. Please try again later.')

# Run the app
if __name__ == '__main__':
    news_tab()
