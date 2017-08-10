
import pandas as pd
import numpy as np


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import re

def sentiment_extract(id): 
    
    name_file= 'Comments_tiny_homes'+id+'.csv'    
    d1=pd.read_csv(name_file,encoding = "ISO-8859-1") # encoding=utf8   
    ds=''              
    for i in range(len(d1)):
        ds=ds+'. '+str(d1['comments'].iloc[i])  
    ds=re.sub('toilets','toilet',ds)
     
     
    tiny_home_features=['architecture', 'bathroom', 'bed', 'bedroom', 'concrete',
                        'cost', 'design', 'furniture', 'home', 'house', 'idea', 'kitchen',
                        'ladder', 'life', 'light', 'neighbor', 'place', 'power', 'roof', 'room',
                        'shower', 'space', 'stairs', 'toilet', 'view', 'wall', 'washroom',
                        'water', 'wood','stairwell','storage','apartment','plywood',
                        'floor','night','glass','metal','garage','area','ceiling','size'
                        ,'window','door'] # updated July 30 17
    feature_sentiment={}      
    words_counter2={} # number of a given word (from ist of most comon) in the text
     
    sent_tokens = sent_tokenize(ds)
    for feature in tiny_home_features:
        for sent in sent_tokens:
            my_sent_sentiment = TextBlob(sent)
            if feature in sent:
                if (feature or (feature+'s')) in feature_sentiment:
                    feature_sentiment[feature]+=my_sent_sentiment.sentiment.polarity
                    words_counter2[feature]+=1
                else:
                    feature_sentiment[feature]=my_sent_sentiment.sentiment.polarity
                    words_counter2[feature]=1
    feature_sentiment_corr={k: feature_sentiment[k]/words_counter2[k] for k in words_counter2.keys() & feature_sentiment}           
    temp_data_frame=pd.DataFrame(feature_sentiment_corr,index=['0'])
    return temp_data_frame
     
my_feature_sentiment=sentiment_extract('1')
tiny_names=list(map(lambda x: str(x),range(2,155)))
#tiny_names=list(map(lambda x: str(x),range(2,22)))
for tiny_name in tiny_names:
    my_feature_sentiment=my_feature_sentiment.append(sentiment_extract(tiny_name),ignore_index=True)

#my_feature_sentiment.to_csv('microapartment_feature_sentiment4_july22_30.csv') 
my_feature_sentiment.to_csv('my_feature_sentiment4_july22_30.csv')   
 