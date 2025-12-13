from scipy import stats
import pandas as pd 
import numpy as np

randframe = pd.DataFrame(np.random.randn(1000,3))



# calculate z-score for column A 
z=np.abs(stats.zscore(randframe)) 

# identify outliers 
threshold =1.5
outliers = randframe[z > threshold]

res1=outliers.dropna(how='all') 
res2=outliers.dropna(how='any') 
