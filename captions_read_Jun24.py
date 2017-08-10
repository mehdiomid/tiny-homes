# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 20:25:22 2017

@author: Mehdi
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
df1=pd.read_csv('video_dates.csv')
videoids=df1['videId']
all_video_captions=pd.DataFrame(columns=["videoid","caption","link_in_caption"])
for videoid in videoids:
    url_page="https://www.youtube.com/watch?v="+videoid
    page = requests.get(url_page)
    soup = BeautifulSoup(page.text, "lxml")
    video_caption=list(soup.find_all('div', attrs={'id': 'watch-description-text'}))
    if (len(video_caption)>=1):
        video_caption_text=video_caption[0].text
        link_in_caption_text=video_caption[0].select('a')
        if (len(link_in_caption_text)>=1):
            no00=re.findall('href=".*\/"',str(link_in_caption_text[-1]))
            if (len(no00)>=1):
                link_in_caption=re.sub('"|href=','',no00[0])
            else:
                link_in_caption=''
    else:
        link_in_caption=''
        video_caption_text=''
    all_video_captions=all_video_captions.append({
                                                  "videoid":videoid,
                                                  "caption":video_caption_text,
                                                  "link_in_caption":link_in_caption
                                                  }, ignore_index=True)
all_video_captions.to_csv('captions.csv')    