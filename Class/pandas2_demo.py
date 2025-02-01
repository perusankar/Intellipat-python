import pandas as pd

tup = (1,2,3,4,5,6,7,8,9,10)
listtest = [1,2,3,4,5,6,7,8,9,10]
settest = {1,2,3,4,5,6,7,8,9,10}

series1 = pd.Series(tup)
print(series1)
series2 = pd.Series(listtest)
print(series2)
series3 = pd.Series(list(settest))
print(series3)

dict1 = {
    'Name' : ['Peru','Nathan','Nitin','Rajesh'],
    'Age': [34, 35, 45,34],
    'Hobby': ['Soccer', 'Tennis', 'Pickleball', 'Chess'],
    'Group' : 'Agg'
}

Series = pd.Series(dict1)
print(Series)

dict2 = {
    'Name' : 'Peru',
    'Age': 34,
    'Hobby': 'Soccer'
}

Series = pd.Series(dict2)
print(Series)