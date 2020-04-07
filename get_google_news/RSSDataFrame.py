import pandas as pd
from bs4 import BeautifulSoup
import requests


class RSSDataFrame:
    
    """
    Container for article titles, links,
    publish times, and sources scraped 
    from Google News RSS feeds.
    """

    def __init__(self, language, topic, location):

        """
        Takes a location name (string dtype), 
        language (string dype), and a topic of 
        interest (string dtype) to construct
        a simple query to Google News RSS feed.
        """
        
        self.location = location
        self.language = language
        self.topic = topic
        self.url =  "https://news.google.com/rss/search?q={}&gl={}&hl={}-{}&ceid={}:{}-{}".format(
            topic, 
            location,
            language, 
            location, 
            location,
            language, 
            location
            )
            
    def get(self):
        self.list_of_titles = []
        self.list_of_article_links = []
        self.list_of_pubdates = []
        self.location_id_for_articles = []

        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'lxml')
        self.xml = str(list(self.soup)).split('<item><title>')

        for i in range(len(self.xml[1:-1])):
            self.list_of_titles.append(self.xml[i+1].split("</title>")[0])
            self.list_of_article_links.append(self.xml[i+1].split("</title><link/>")[1].split("<guid ispermalink")[0])
            self.list_of_pubdates.append(self.xml[i+1].split("</guid><pubdate>")[1].split("</pubdate>")[0])
            self.location_id_for_articles.append(self.location)

        self.df = pd.DataFrame([self.list_of_titles, 
                                self.list_of_article_links, 
                                self.list_of_pubdates, 
                                self.location_id_for_articles]).T

        self.df.columns = ["Title","URL","Published","Location"]
        self.df["Source"] = self.df["Title"].str.split("-").str[-1]
        return self.df