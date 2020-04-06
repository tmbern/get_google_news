# get_google_news
A Python module to load Google News RSS feeds into pandas DataFrames
Takes a location and topic of interest as inputs.
Returns a pandas DataFrame of article results

### Installation

```

pip install -i https://test.pypi.org/simple/ get-google-news==0.1

```

### Examples

```python

from get_google_news import RSSDataFrame

df = RSSDataFrame("California","Tacos").get()

another_df = RSSDataFrame("Canada","Hockey")

```
