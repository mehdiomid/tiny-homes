---
date: "April 30, 2017"
---


## Prediction of public interest in tiny homes by analyzing youtube comments

**By Mehdi omidghane**

### Introduction

In the last decade, a social movement known as tiny living, has gained popularity among many people who are seeking a simpler lifestyle. Many are leaving their typical houses and downsizing to a smaller, yet efficient living space. The reasons include more financial freedom, more time available and maintaining an environmentally sustainable lifestyle.  Although tiny houses are more attractive in larger cities, for example Tokyo, New York, or San Francisco where the price of housing is high, however it is popular in other areas. Here in Edmonton, in the Faculty of Arts at the University of Alberta, are advertising and inspiring micro-living in the province.  The reason I chose this is because I am an advocate of sustainable living and am intrigued by the creativity techniques used in these spaces.
	
There are many sources available on the web for tiny houses that explore different floor plans and creative uses of micro-space. Among them, are videos posted to YouTube by Kirsten Dirksen, co-founder of faircompanies. In her channel, Kirsten travels around the globe and creates videos of people that have chosen to live in tiny houses. Her videos are popular and have views in orders of several hundreds of thousand to millions of views per each episode. Many of the viewers are, as expected, are people who are interested in this movement and are looking to perhaps transition to tiny living. A quick look at the comments section reflects this and shows that the viewers are genuine (not so-called 'trolls'), engaged, either liking the tiny house or are critical of some aspects of it. My project is to take the videos on Kirsten's channel that showcase tiny houses, and based on the comments, rank the videos on how well each tiny space is received. In order to do that, using web-scraping techniques, the videos are chosen and based on word inquires in the comments, the videos are sorted.

### Method

##### Data collection

Kristen' channel (<https://www.youtube.com/channel/UCDsElQQt_gCZ9LgnW-7v-cQ>) currently contains 12 playlists from which two are focused on tiny living: 

*Micro apartments (21 videos)

*Tiny homes (150 videos)

By using a Google API obtained from here (<https://console.developers.google.com>) and some programming in R, all the comments of the videos in the playlist as well as their characteristics such as name of the users, publication time, etc. were extracted and stored in csv files using a write command.

#### Data analysis

All data files (csv files) collected in the previous step were then loaded to R to search for specific words that are possibly indicating a positive perception about the tiny houses. As a preliminary test, here I have searched for "good", "love", "creative", "brilliant", "cute", "amazing", "interesting", "cool", "not bad" and "creativity". As we have data regarding the date at which the videos were published, we can then make a graph showing the total number of positive words over time. This can be interpreted as the measure of tiny homes' popularity over time.

Also, we can find the total number of words such as "bad", "not good", "hate", "hole", "prison" to measure how much people hate the concept of tiny homes over time.

#### Future work

The results here are very rough by all means. As a project proposed for The Data Incubator program, I plan to continue this by looking at the possible relationship between user profiles and their interest/ repulsion against the tiny homes. Statistical analysis should be conducted to identify the true inferences.  Ultimately, a statistical model such as regression will be used to model these relationships and to predict the upcoming trends.




I