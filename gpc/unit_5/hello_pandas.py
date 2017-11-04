
import pandas as pd
import numpy as np

df = pd.read_csv('../data/animals.csv', delimiter = ',' )
#print df.ix[0]



obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
print uniques
print obj.value_counts()
mask = obj.isin(['b','c'])
print mask
print obj[mask]
