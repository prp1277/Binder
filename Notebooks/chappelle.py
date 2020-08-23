# This code is not my own, I have adapted it from
# https://github.com/adashofdata/nlp-in-python-tutorial
#%%
import requests
from bs4 import BeautifulSoup
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text
import re
import string
import pandas as pd
from collections import Counter

pd.set_option("max_colwidth", 150)

# %%
def url_to_transcript(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find(class_="post-content").find_all("p")]
    print(url)
    return text


urls = [
    "https://scrapsfromtheloft.com/2018/01/03/dave-chappelle-equanimity-2017-full-transcript/",
    "https://scrapsfromtheloft.com/2018/01/03/dave-chappelle-the-bird-revelation-2017-full-transcript/",
    "https://scrapsfromtheloft.com/2017/05/19/dave-chappelle-worth-2004-full-transcript/",
    "https://scrapsfromtheloft.com/2017/05/19/dave-chappelle-killin-softly-2000-full-transcript/",
    "https://scrapsfromtheloft.com/2017/04/20/dave-chappelle-deep-heart-texas-2017-full-transcript/",
    "https://scrapsfromtheloft.com/2017/04/11/dave-chappelle-age-spin-2017-full-transcript/",
    "https://scrapsfromtheloft.com/2020/06/19/dave-chappelle-hbo-comedy-half-hour-1998-transcript/",
    "https://scrapsfromtheloft.com/2019/08/29/dave-chappelle-sticks-stones-epilogue-punchline-transcript/",
    "https://scrapsfromtheloft.com/2018/09/23/david-chappelles-snl-monologue-2016-transcript/",
]

specials = [
    "Equanimity",
    "The_Bird_Revelation",
    "For_What_It's_Worth",
    "Killin'_Em_Softly",
    "Deep_In_the_Heart_of_Texas",
    "The_Age_of_Spin",
    "HBO_Comedy_Half-Hour",
    "Sticks_and_Stones:Epilogue",
    "SNL_Monologue",
]
transcripts = [url_to_transcript(u) for u in urls]

# %%
for i, c in enumerate(specials):
    with open("data/transcripts/Chappelle/" + c + ".txt", "wb") as file:
        pickle.dump(transcripts[i], file)
# %%
for i in transcripts:
    transcripts.index(i)

transcripts[:]

# %%
chappelle_df = pd.DataFrame(transcripts)
chappelle_df
