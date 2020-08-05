# DATA ANALYSIS USING PYTHON AND ELASTICSEARCH

## Introduction
This project was based in analize one data set in a faster way using elasticsearch to index all data. Why elasticsearch? **Elasticsearch** is a distributed, open source analytics and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. And the data set that we used was about taxis trips, then we needed to make graphs using geopoints by that reasons we must put it in applying indexation with Elasticsearch.

In the other hand, for the visualization, we made a heatmap to show the most frecuent places to pickup people and the same with dropoff. These maps can be filter in months or anual mode, but also we made an data visualization using **Tableau**

## Pipline
### Steps for normal pipline:
![Steps](https://escueladedatos.online/wp-content/uploads/2019/09/pipeline.png)

### Our pipline for the project
![pipline](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/pipline.png?raw=true)

[Simple pipline](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/pipeline.pdf)


**Define**

Data-driven projects should start by defining the problem they want to solve and their actions. It is at this stage that you ask questions and come up with the purposes of your project. In our case the question was: Where and in which month of the year the requests for taxis are more frequent? With this we solve a problem for many companies of taxi services, since many times they do not know how to create their travel plans and also do not know where to offer the services. By doing this analysis we obtain frequent places of applications and also destinations, so the company can know where to establish and also where to establish defined destinations.

As a second point you will also know in which month the trips are longer and with that same give warning about the gasoline expenses in those months, in the same way that month taxis are more requested.

**Searching**

While the definition phase of the problem suggests which data you will need, searching for this data is another step, with much or little difficulty, depending on the problem. There are many tools and techniques to do that: from a simple question on your social media, to using tools like a search engine, open data portals or a request for access to information asking for data that is available in that government institution. In our case as we were going to do a data analysis on where the request for taxis is more frequent, we decided to look for a [dataset](https://www.kaggle.com/mnavas/taxi-routes-for-mexico-city-and-quito?select=mex_clean.csv) that can give us geopoints and times as well as frequencies, for that we use **Kaggle**.

**Collecting**

Producing data can be a short and easy task, or a long and complex one. The important thing is to design a replicable method and choose the most appropriate way for the project, since its scope and conclusions will depend on that choice. In our case the collection of data is done from a previously downloaded dataset, since records are already kept and in addition the mestro asked us that the user or the person who wants to do the same analysis can replicate it and this can happen, simply changing the data for others as long as they respect the names of the columns, the formats and the name of the .csv. That is to say that anyone can edit the csv and add more data and the program will continue to do the analysis with each year that is added.

**Verify**

Getting the data does not mean that the problem is solved. It is necessary to verify whether your information is valid, as well as to review the metadata and methodology with which this set of information was collected. In our case, during the verification we realized that the travel time data were unbalanced or as in the data science we say **outliers**, because for more than seconds it was, if we passed them to minutes they became more than 10,000 hours, since we identified that the cause was that the taxi drivers forgot to turn off the GPS and this continued measuring the time, so once identified and checked that the other columns were fine and that they were not going to serve us for analysis, we went to do the data cleaning.

**Cleanning**

It is very common for data to be obtained and validated to be in disarray and to have formatting problems: duplicate rows, column names that do not match the records, values that contain rare characters or that prevent computer processing, and others. As in our cases, the formats of dates and times in which taxi drivers were required were in the same column, which we could not leave them alone, since we needed to analyze it separately, date and time, by the issue of filters. What we did was separate into two new columns called, pickup_time and pickup_date the data, the same for the dropoff, in addition we did a cleaning of outliers, since we noticed that there were only 5 drivers that arrived at the million in the part of journey duration, so a filter was applied to the columns and rows that had a time greater than 9999 seconds were removed. Then we created a new . csv that was already clean.

**Analyze**
This is the part where we get knowledge about the problem that we defined at the beginning. By putting our statistical and mathematical skills into practice, we can interview a data set like any journalist interviews their sources. In our case, our first analysis was to see on a map the most frequent places so we needed to take out the places that were repeated, how to do that if we only have locations? We had to count the number of times the dots were repeated and put them in a dataframe. The second analysis was to take out the average time it took to travel per month. The third was to take out the average mileage per month. These analyses will give the company an idea of the months in which they must invest more in the maintenance of taxis without being affected, as well as opportunities for improvements, all this measuring data per month.

**Visualization**

It is necessary to present the data: talk to your audience so that they know the questions you were looking to answer and the means that has allowed you to reach certain conclusions or start a conversation. In our case we mentioned that we made an interactive map of heat with which the user can investigate all areas of Mexico, exploring the frequency of trips with the intensity of color, in addition we made graphics that were shown below.


