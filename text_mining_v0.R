library(tm)
library(SnowballC)
library(wordcloud)

# We perform a series of operations on the text data to simplify it.
#First, we need to create a corpus.

doc <- Corpus(VectorSource(data_file$comments))

#Next, we will convert the corpus to a plain text document.
###jeopCorpus <- tm_map(jeopCorpus, PlainTextDocument)
#Then, we will remove all punctuation and stopwords. Stopwords are commonly
#used words in the English language such as I, me, my, etc. You can see the
#full list of stopwords using stopwords('english')
#
#Transform to lower case (need to wrap in content_transformer)
doc <- tm_map(doc,content_transformer(tolower))
doc <- tm_map(doc, removePunctuation)
doc <- tm_map(doc, removeWords, stopwords('english'))
doc <- tm_map(doc, removeWords, c("also", "the", "just","but",
                                                "this","that","its","dont",
                                                "can","man","done","get"))



#Next, we will perform stemming. This means that all the words are converted 
#to their stem (Ex: learning -> learn, walked -> walk, etc.). This will ensure
#that different forms of the word are converted to the same form and plotted only
#once in the wordcloud.

doc <- tm_map(doc, stemDocument)
#Now, we will plot the wordcloud.

wordcloud(doc, max.words = 50,scale=c(3,.5), random.order = FALSE,colors=brewer.pal(5,'Dark2'))



dtm <- DocumentTermMatrix(doc)
freq <- colSums(as.matrix(dtm))
d <- data.frame(word = names(freq),freq=freq)

p <- ggplot(subset(d, freq>30), aes(word, freq))
p <- p + geom_bar(stat='identity')
p <- p + theme(axis.text.x=element_text(angle=45, hjust=1))
p

#Next, we sort freq in descending order of term count:
#create sort order (descending)
ord <- order(freq,decreasing=TRUE)

#Then list the most and least frequently occurring terms:
#inspect most frequently occurring terms
freq[head(ord,10)]
#The results make sense: the top 6 keywords are pretty good descriptors of what the text is about

#we can check for correlations between some of these and other
#terms that occur in the corpus.  In this context, correlation 
#is a quantitative measure of the co-occurrence of words in multiple documents.

#The tm package provides the findAssocs() function to do this.

findAssocs(dtm,'beautiful',0.2)


#Do sentiment analysis 
library('syuzhet')

file_list <- list.files() # reading all CSV files
for (i in 1:(length(file_list))) { 
  data_file <- read.csv(file_list[i],header=TRUE,stringsAsFactors=FALSE )
  d<-get_nrc_sentiment(data_file$comments)
  td<-data.frame(t(d))

  td_new <- data.frame(rowSums(td))#[1:nrow(data_file)]))
  #The function rowSums computes column sums across rows for each level of a grouping variable.
  #Transformation and  cleaning
  names(td_new)[1] <- paste0("count",as.character(i))
  if (i==1) {
    td_all<- td_new
  }else{
    td_all <- cbind(td_all,td_new)
  }
}
#
td_all1 <- cbind("sentiment" = rownames(td_all), td_all)
rownames(td_new) <- NULL
td_new2<-td_new[1:8,]
td_new3 <- td_new[9:10,]
#Graph the sentiment analysis in ggplot2
#Visualisation
library("ggplot2")
qplot(sentiment, data=td_new2, weight=count, geom="bar",fill=sentiment)+ggtitle("Comments sentiments")
qplot(sentiment, data=td_new3, weight=count, geom="bar",fill=sentiment)+ggtitle("Comments sentiments")

