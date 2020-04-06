import pandas as pd
from bs4 import BeautifulSoup
import requests

class RSSDataFrame:

    """This function takes a location name (string dtype) and a topic of interest (string dtype). 
    The output is a pandas DataFrame with articles, urls, and publishing times for articles containing the location and topic
    """

    def __init__(self, location, topic):
        self.location = location
        self.topic = topic
        self.url = "https://news.google.com/rss/search?q={}+{}&hl=en-US&gl=US&ceid=US:en".format(self.location, self.topic)

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