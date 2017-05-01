playlistid <- "PL07EC797A2E900CFC"
#
# Your API key obtained via https://console.developers.google.com/ 
API_key='AIzaSyAMIw0Db21b3yT66oEsPRDBTA7mr7ABzQg'
#
# Load the necessary packages
require(curl)
require(jsonlite)
library(ggplot2)

# Base URL for Google API's services and YouTube specific API's
Base_url="https://www.googleapis.com/youtube/v3/" #commentThreads?"

## Extracting all video ids of the channel
for (i in 1:30) {
  if (i==1) {
    urp<- paste0(Base_url,"playlistItems?&part=contentDetails&playlistId=",playlistid,"&key=",API_key)
    resultid <- fromJSON(txt=urp)
    allvid_id<- resultid$items$contentDetails$videoId
    date_published <- resultid$items$contentDetails$videoPublishedAt
    pageToken <- resultid$nextPageToken
  }else{
    urp<- paste0(Base_url,"playlistItems?pageToken=",pageToken,"&part=contentDetails&playlistId=",playlistid,"&key=",API_key)
    resultid <- fromJSON(txt=urp)
    allvid_id_temp<- resultid$items$contentDetails$videoId
    date_published_temp <- resultid$items$contentDetails$videoPublishedAt
    allvid_id <- c(allvid_id,allvid_id_temp)
    date_published <- c(date_published,date_published_temp)
    pageToken <- resultid$nextPageToken
  }
}
allvid_id <- unique(allvid_id)
date_published<- as.Date(unique(date_published))
videoData <- data.frame(videId=allvid_id,published=date_published)
#
## Extracting all the comments for each video Id extracted from the list
filenumber=1
for (videoId in allvid_id) {
  for(i in 1:20){
    if (i==1) {
      url_add <- paste0(Base_url,"commentThreads?","&part=snippet,replies&videoId=",videoId,"&key=",API_key)
    } else{
      url_add <- paste0(Base_url,"commentThreads?","pageToken=",pageToken,"&part=snippet,replies&videoId=",videoId,"&key=",API_key)
    }
    # Perform query
    result<- fromJSON(txt=url_add)
    if (i==1){
      comments <- data.frame(user=result$items$snippet$topLevelComment$snippet$authorDisplayName,comments=result$items$snippet$topLevelComment$snippet$textOriginal)
      pageToken <- result$nextPageToken
    } else{
      next_comments<- data.frame(user=result$items$snippet$topLevelComment$snippet$authorDisplayName,comments=result$items$snippet$topLevelComment$snippet$textOriginal)
      comments <- rbind(comments,next_comments)
      pageToken <- result$nextPageToken
    }
    
  }
  comments_final<-comments #data.frame(comments=unique(comments$comments)) 
  filename <- paste0("Comments_tiny_homes",as.character(filenumber),".csv")
  filenumber <- filenumber+1
  write.csv(file=filename,comments_final)
}

## Reading files to look for special words

file_list <- list.files() # reading all CSV files
words<-numeric(length(file_list))
for (i in 1:(length(file_list))) { 
  i<- 1
  data_file <- read.csv(file_list[i],header=TRUE)
  search_for_neg<- "[Pp]rison|[Hh]ole|[Bb]ad|[Nn]ot good"
  search_for_pos<- "[Gg]ood|[Cc]ute|[Bb]rilliant|[Ll]ove|[Cc]reative|[Nn]ot bad"
  words[i]<-as.numeric(table(grepl(search_for_neg,data_file$comments))[2])
}
g<- ggplot(data.frame(date=date_published,totwords=words),aes(x=date,y=totwords))
g <- g+ geom_point()+geom_smooth(method="lm")+ylim(0,40)
g<- g+ xlab("Date")+ylab("Total No of Words")+ggtitle("A measure of Public Dislike over time")
g


