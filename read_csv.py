import pandas as pd
import findspark
findspark.init()

data=pd.read_csv('./data/ratings_Electronics.csv',names=['userId',''])
print(data.head())