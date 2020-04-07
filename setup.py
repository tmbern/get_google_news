from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="get_google_news", # the name that you will install via pip
    version="0.3.3",
    author="Alex Pakalniskis 3",
    author_email="alexpakalniskis3@gmail.com",
    description="A Python 3 module to load Google News RSS feeds into pandas DataFrames",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/alex-pakalniskis/get_google_news",
    keywords="Google News",
    packages=find_packages() 
)