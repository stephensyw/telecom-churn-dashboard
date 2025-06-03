#%%
 
import pandas as pd

data = {
    'CustomerID': range(1001, 1021),
    'Age': [22, 45, 36, 51, 29, 34, 40, 23, 39, 33, 27, 48, 31, 50, 28, 37, 30, 41, 49, 26],
    'Region': ['East', 'West', 'South', 'East', 'North', 'West', 'South', 'North', 'East', 'West',
               'South', 'East', 'West', 'South', 'North', 'East', 'West', 'South', 'North', 'East'],
    'ServiceType': ['Mobile', 'Internet', 'Mobile', 'Internet', 'TV', 'Mobile', 'Internet', 'TV', 'Mobile', 'TV',
                    'Internet', 'Mobile', 'TV', 'Mobile', 'Internet', 'Mobile', 'Internet', 'TV', 'Mobile', 'TV'],
    'MonthlySpend': [30, 55, 40, 65, 50, 45, 70, 35, 60, 55, 38, 42, 58, 47, 49, 51, 64, 39, 41, 53],
    'TenureMonths': [12, 24, 36, 18, 6, 9, 48, 30, 21, 33, 27, 15, 22, 29, 34, 45, 19, 20, 39, 13],
    'Churned': ['No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes',
                'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)
df.to_csv('dataset.csv', index=False)
df.head()

