import streamlit as st
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from newspaper import Article
import nltk

# Download NLTK resources
nltk.download('punkt')

def fetch_news_search_topic(query):
    site = f'https://news.google.com/rss/search?q={query}'
    op = urlopen(site)
    rd = op.read()
    op.close()
    sp_page = soup(rd, 'xml')
    news_list = sp_page.find_all('item')
    return news_list

def display_news(news_list):
    st.title("Google News Scraper")
    for news in news_list:
        st.subheader(news.title.text)
        st.write(f"**Published Date:** {news.pubDate.text}")
        article = Article(news.link.text)
        try:
            article.download()
            article.parse()
            article.nlp()
            st.write(article.summary)
            st.image(article.top_image, caption='Article Image', use_column_width=True)
            st.markdown(f"[Read more]({news.link.text})")
            st.write("---")
        except Exception as e:
            st.warning(f"Failed to extract article details: {e}")

def run():
    st.sidebar.title("Google News Scraper")
    query = st.sidebar.text_input("Enter a topic to search:")
    if st.sidebar.button("Search"):
        if query:
            news_list = fetch_news_search_topic(query)
            display_news(news_list)
        else:
            st.warning("Please enter a search query")

if __name__ == "__main__":
    run()
