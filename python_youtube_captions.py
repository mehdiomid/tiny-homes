# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 18:04:25 2017

@author: Mehdi
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
df1=pd.read_csv('video_dates.csv')
videoids=df1['videId']
all_video_captions=pd.DataFrame(columns=['videoid','caption','link_in_caption'])
for videoid in videoids:
    url_page="https://www.youtube.com/watch?v"+videoid
    page = requests.get(url_page)
    soup = BeautifulSoup(page.text, "lxml")
    video_caption=list(soup.find_all('div', attrs={'id': 'watch-description-text'}))
    video_caption_text=video_caption[0].text
    link_in_caption_text=str(video_caption[0].select('a')[0])
    no00=re.findall('href=".*\/"',link_in_caption_text)[0]
    link_in_caption=re.sub('"|href=','',no00)
    df_video=pd.DataFrame([videoid,video_caption_text,link_in_caption],columns=['videoid','caption','link_in_caption'])
    all_video_captions.append(df_video, ignore_index=True)
    



    
    
    