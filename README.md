# Find cues to prepare a career in DataScience in Stackoverfolw public survey 2017
Find the story on [Medium](https://medium.com/@sebastien.villard/scientist-to-data-scientist-468c906c5756?source=friends_link&sk=bb9fa0018d4235348921363bc023d858)  
_S.Villard June 2020_

You'll find the main notebook [there](./code/StackPublicSurvey.ipynb) in ```./code```. This notebook calls different function located in ```./code/stack_functions.py```: ```convert2USD``` and ```getChoices```  
The dataset (data and schema) used in this exmaple is located in ```./DataSets/StackOverflow/```: Satck Overflow developer survey results from 2017 (see results [here](https://insights.stackoverflow.com/survey/2017)). 


## We are trying to answer the following questions:

1. How do I break into the field? We focused our analysis on recent-hires only (professional that changed job within 4 years)
2. Beyond the advice given by the respondents, we wanted to know what education/training helped the recent-hires get their new job? 
3. How this training relates to job satisfaction and Salary?
4. Is that still true for the subsample of data scientists?
5. Taking Salary as a measure of success, how well can we predict an individual's salary?
    
## Data wrangling:

1. Select only actual Professional.
2. Regarding Salary:  
- we filtered out data with missing salaries
- we converted salary into USD for comparison using the ```forex_python``` module ([see Project description](https://pypi.org/project/forex-python/). This module is used by ```stack_functions.convert2USD_today```
> for speed we chose to a fix exchange rate as of July 8th, 2020 store in ```./DataSets/StackOverflow/rates_20200708.csv``` called by ```convert2USD```
- we filtered outliers' salaries from extremely high and extremely low values.

