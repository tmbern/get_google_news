# get_google_news
A Python module to load Google News RSS feeds into pandas DataFrames
Takes a language code (two-letter), topic of interest (string), and country code (two-letter) as inputs.
Returns a pandas DataFrame of article results

### Installation

```

pip install -i https://test.pypi.org/simple/ get-google-news==0.3.3

```

### Usage

```python

from get_google_news import RSSDataFrame

template = RSSDataFrame(<LANGUAGE CODE>,<TOPIC OF INTEREST>, <REGION>).get()

example = RSSDataFrame("en","covid19", "US").get()

another_example = RSSDataFrame("fr","covid19", "CA").get()


```
