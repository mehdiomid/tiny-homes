# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:48:19 2017

@author: Mehdi
"""

import pandas as pd
import matplotlib.pyplot as plt
sentimet_table=pd.read_csv('my_feature_sentiment2.csv')

plt.figure()
plt.ylabel("polarity")
plt.xlabel('id')
plt.title('Design')
plt.axis([0, 160, -0.5, 1])
plt.scatter(range(len(sentimet_table)),sentimet_table['design'],c=sentimet_table['design'],s=50)


vid_dates=pd.read_csv('video_dates__.csv')
videoiid=vid_dates['videId']

best_design_pvalue=max(sentimet_table['design'])
best_design_index=sentimet_table.idxmax()['design']

best_design_videoid=videoiid[best_design_index]
print('Best {} video is\n https://www.youtube.com/watch?v={}'.format('design',best_design_videoid))
###^^^^^^^^^^^^^^^^^^^^^^^^ WORST
worst_design_pvalue=min(sentimet_table['design'])
worst_design_index=sentimet_table.idxmin()['design']

worst_design_videoid=videoiid[worst_design_index]


''' For washroom'''
plt.figure(2)
plt.ylabel("polarity")
plt.xlabel('id')
plt.title('Washroom')
plt.axis([0, 160, -0.5, 1.1])
plt.scatter(range(len(sentimet_table)),sentimet_table['toilet'],c=sentimet_table['toilet'],s=50)
plt.savefig('best_and_worst_washroom.png')
plt.close()

best_washroom_pvalue=max(sentimet_table['toilet'])
best_washroom_index=sentimet_table.idxmax()['toilet']
best_washroom_videoid=videoiid[best_washroom_index]
print('Best {} video is\n https://www.youtube.com/watch?v={}'.format('washroom',best_washroom_videoid))


######################################################
#                 Noun Phrases

videoid=127
name_file= 'Comments_tiny_homes'+str(videoid)+'.csv'    
d1=pd.read_csv(name_file,encoding = "ISO-8859-1")
ds=''              
for i in range(len(d1)):
     ds=ds+'. '+str(d1['comments'].iloc[i])
     
wiki = TextBlob(ds)
wiki.noun_phrases

design_phrase=[p for p in wiki.noun_phrases if 'design' in p]
washroom_phrases=[p for p in wiki.noun_phrases if 'toilet' in p]+[p for p in wiki.noun_phrases if 'washroom' in p]
kitchen_phrase=[p for p in wiki.noun_phrases if 'kitchen' in p]