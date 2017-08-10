from flask import Flask, render_template, request

import pandas as pd
import numpy as np
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.charts import Bar, show, output_file



from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string




app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
 feature_names=list(map(lambda x: str(x),range(1,155)))
 
 
 def create_figure(current_feature_name, bins=20):
     
     
     name_file= 'data\Comments_tiny_homes'+current_feature_name+'.csv'    
     d1=pd.read_csv(name_file,encoding = "ISO-8859-1") # encoding=utf8   
     ds=''              
     for i in range(len(d1)):
         ds=ds+''+str(d1['comments'].iloc[i])  

     word_tokens = word_tokenize(ds)
     word_tokens = list(map(lambda x: x.lower(), word_tokens))
# stop_words = set(stopwords.words('english'))
     punctuation = list(string.punctuation)
     stop = stopwords.words('english') + punctuation + [
     'the', 'this','can','could','that','n\'t','would','...','\'s',
     '\'\'','u+009f','``','f0','\'m','look','home','put','house','get','need','think'
     'need','want','great','good','beautiful','nice','u+043e','love','living','see','small'
     ,'much','one','make','even','make','really','see','also','better','like'
     'live','looks','think','video','way','use','well','like','made','use','work',
     'many','time','things','move','goes','best','always','find','thanks',
     'videos','interesting','kristen','little','live','amazing','\'d',
     'tiny','guys','got','know','take','film','thank','thanks','us','loved',
     'every','keep','watching','back','u+0091','using','set','people','new'
     'still','stuff','thing','ca','cool','happens','things','might','u+008d','still','go'] 
     
     filtered_words = [w for w in word_tokens if not w in stop]
     count = Counter(filtered_words)
 
     p=pd.DataFrame(count.most_common(15),columns=['word','count'])
     plot = Bar(p, 'word', values='count', title="Word frequency",color='count',legend=None)
	
     return plot
     
 def video_captions(current_feature_name):
     captions=pd.read_csv('data\captions_v_2.csv',encoding = "ISO-8859-1")
     return captions.iloc[int(current_feature_name)-1]['caption']
                          
 def video_title(current_feature_name):
     videotitle=pd.read_csv('titles.csv',encoding = "ISO-8859-1")
     return videotitle.iloc[int(current_feature_name)-1]['title']
                            
 def sentiment_plot(current_feature_name):
     sentimet_table=pd.read_csv('my_feature_sentiment2.csv')
     labels=['architecture','bathroom','bed', 'bedroom','concrete','cost',
             'design','furniture','home','house','idea', 'kitchen','ladder',
             'life', 'light','neighbor','place','power','roof','room', 
             'shower', 'space', 'stairs','toilet','view','wall',
             'washroom','water','wood']
             
     my_polarity=list(sentimet_table.iloc[int(current_feature_name)])[1:]
     data_0=pd.DataFrame({'features':labels ,'polarity':my_polarity})
     #plot2=scatter(range(len(sentimet_table)),sentimet_table['design'],c=sentimet_table['design'],s=50)
     plot2 = Bar(data_0, 'features', values='polarity', title="polarity",color='polarity',legend=None)
     return plot2
 def sentiment_all():
     sentimet_table=pd.read_csv('my_feature_sentiment2.csv')
     sent_new=sentimet_table.drop('Unnamed: 0',1)
     average_sent=sent_new.mean(axis=1,skipna=True)
     
     plot4=figure(title="All features",x_axis_label='id',y_axis_label='polarity')
     plot4.scatter(range(len(average_sent)),average_sent,size=10, color='blue')
     
     
     return plot4
     
 current_feature_name = request.args.get("feature_name")
 if current_feature_name == None:
     current_feature_name = "1"

	# Create the plot
 plot = create_figure(current_feature_name, 10)
 plot2 = sentiment_plot(current_feature_name)
 plot4= sentiment_all()
 caption=video_captions(current_feature_name)
 title11=video_title(current_feature_name)
 
 
#**********************************************************     
 

 # Generate the script and HTML for the plot
 script, div = components(plot)
 script2, div2 = components(plot2)
 script4, div4 = components(plot4)
 
 js_resources = INLINE.render_js()
 css_resources = INLINE.render_css()
 
 
 
 
 #******************************************************
 return render_template('index4.html',plot_script=script,
                        plot_div=div,
                        plot_script2=script2,
                        plot_div2=div2,
                        plot_script4=script4,
                        plot_div4=div4,
                        js_resources=js_resources,
                        css_resources=css_resources,
                        feature_names=feature_names,
                        current_feature_name=current_feature_name,
                        caption11=caption,
                        title11=title11)
 
#******************************************************* 

 
     
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
#    app.run(debug=True, use_reloader=True)

