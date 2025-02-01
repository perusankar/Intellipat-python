import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

li = [11,22,33,'Kartik','James',56.8,'Python']
print(li)
print(type(li))

new_se = pd.Series(['Kabir','Maxime','Mahesh','Riya','Karthick'])
print(new_se)  #08:30

se = pd.Series(li)  #Creating a series with a list.
print(se)
print(se[2:5])   #[start index: end_index+1]

fd  = [['Kabir',34],['Maxime',56]]
rf = pd.DataFrame(fd,columns=['Name','Age'])
print(rf)

di_data = {
    'Cars':['BMW','KIA','MG','Tata','Nissan','BYD'],
    'Price':['56 Lakhs','23 Lakhs','30 Lakhs','12 Lakhs','15 Lakhs','40 Lakhs'],
    'Model':[2024,2021,2022,2024,2023,None]

}
dff = pd.DataFrame(di_data)
print(dff)

print(dff.loc[1])
print(dff.iloc[2:5,:1])

new_data = {
    'Emp_Name':['Kabir','Mahesh','Phanendharnadh','Preethi','Maxime','Varsha'],
    'Emp_ID':[1021,1014,1045,1945,1123,1432],
    'Salary':[34000,45000,54000,39000,76000,90000],
    'Designation':['ML Engineer','Data Analyst','Research Analyst','AI Engineer','SDE','Business Analyst'],
    'Shift_timings':['9-5','10-7','11-8','9-5','12-9','8-4']
}

vv = pd.DataFrame(new_data)

print(vv)

print(vv['Designation'])
