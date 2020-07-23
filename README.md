Find the story on [Medium](https://medium.com/@sebastien.villard/scientist-to-data-scientist-468c906c5756?source=friends_link&sk=bb9fa0018d4235348921363bc023d858)  
_S.Villard June 2020_

## Table of Contents
1. [Installation](#Installation)
2. [Project Motivation](#Project_Motivation)
3. [File Descriptions](#File_Descriptions)
4. [Results](#Results)
5. [Licensing, Authors, Acknowledgements](#Licensing,_Authors,_Acknowledgements)

___
# __Installation__
 - We used the standard ```numpy```, ```pandas```, ```matplotlib```, ```seaborn``` libraries
 - We used ```IPython.display.Markdown``` for better rendering of text results
 - We converted salary into USD for comparison using the ```forex_python``` module ([see Project description](https://pypi.org/project/forex-python/). This module is used by ```stack_functions.convert2USD_today```
> for speed we chose to a fix exchange rate as of July 8th, 2020 store in ```./DataSets/StackOverflow/rates_20200708.csv``` called by ```convert2USD```
 - We used [```sklearn```](https://scikit-learn.org/stable/) for the salary prediction section.
 
# __Project Motivation__
The stackoverflow public survey 2017 gives a unique opportunity to see what would software developpers recommend to break into the field. For someone like me that is trying to switch career that dataset become particularly interesting.
In this analysis we are trying to answer the following questions:
- How do I break into the field? We focused our analysis on recent-hires only (professional that changed job within 4 years)
- Beyond the advice given by the respondents, we wanted to know what education/training helped the recent-hires get their new job? 
- How this training relates to job satisfaction and Salary?
- Is that still true for the subsample of data scientists?
- Taking Salary as a measure of success, how well can we predict an individual's salary?


# __File Descriptions__
You'll find the main notebook [there](./code/StackPublicSurvey.ipynb) in ```./code/```. This notebook calls different function located in ```./code/stack_functions.py```: ```convert2USD``` and ```getChoices``` 

The dataset (data and schema) used in this exmaple is located in ```./DataSets/StackOverflow/```

# __Results__

## how to break into the field?
> __64.59%__ of recent-hires recommend _taking onlines course_  
but only __30.33%__ took online course prior to landing their new job!<br/>
__50.67%__ of recent-hires have a __Bachelor's degree__ as highest degree

## effect of training on job statisfaction and salary?
> We did not find any impact of the training method on neither job satisfaction nor salary 

## what about data scientist specifically?
> The same conclusions remain true when we consider the data scientist only<br/>
Note that the subsample of data scientist is relatively small (435 observations)

## salary prediction based on this dataset
> A linear model based on Support Vector Regression does a decent job at predicting the salary of the respondents: __69.6%__ of the variance of the salary expressed in USD can be accounted for with linear model comprised of 3 numerical variables and 1066 categorical variables.  

> __Country of residence__ (working place) and __years of coding__ look particularly important in the prediction of the salary.


# __Licensing, Authors, Acknowledgements__
 - Satck Overflow developer survey results from 2017 (see results [here](https://insights.stackoverflow.com/survey/2017))
 - We followed the guidelines provided on [Scikit Learn tutorial page](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html).
 - The cross-validation method was based on a ["NPL with Python for Machine Learning Essential Training"](https://www.linkedin.com/learning/nlp-with-python-for-machine-learning-essential-training?trk=learning-serp_learning_search-card&upsellOrderOrigin=homepage-learning_learning-search-bar_search-submit)