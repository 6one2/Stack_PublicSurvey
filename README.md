# Find cues to prepare a career in DataScience through Stackoverfolw public survey

_this is my project #1 for my nanodegree in DataScience @ Udacity_  
_S.Villard June 2020_

You'll find the main notebook [there](./code/StackPublicSurvey.ipynb) in ```./code```. This notebook calls different function located in ```./code/stack_functions.py```: ```convert2USD``` and ```getChoices```  
The dataset (data in schema) used in this exmaple is located in ```./DataSets/StackOverflow/```: Satck Overflow developer survey results from 2017 (see results [here](https://insights.stackoverflow.com/survey/2017)). 



## We are trying to answer the follwing questions:

1. How do I break into the field?  
2. What are the placement and salaries of thoses who attended a coding bootcamp?  
3. How well can we predict an individual's salary? What aspect correlate well to salary?  
4. How well can we predict an individual's job satisfaction? What aspects correlate well to job satisfaction?
    
## We focus or analysis by preparing our data:

1. Select only actual Professional.
2. Regarding Salary:  
- we filtered out data with missing salaries
- we converted salary into USD for comparison using the ```forex_python``` module ([see Project description](https://pypi.org/project/forex-python/). This module is used by ```stack_functions.convert2USD```

