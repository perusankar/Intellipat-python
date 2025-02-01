import pandas as pd

list1 =  range(10)

series1 = pd.Series(list1)

series1.loc[5] = 200


series1 = series1.drop(series1.index[1])

print("First 5 is " +str(series1.head(5)))
print("Last 5 is " +str(series1.tail(5)))

list3 =  [1,2,3,4,5]
list4 =  [10,20,30,40,50]

series3 = pd.Series(list3)
series4 = pd.Series(list4)

print(pd.concat([series3,series4],ignore_index=True))