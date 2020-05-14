## ...............................LIFE CYCLE OF PROJECT..................................
## 1. Data Analysis
## 2.Feature Engineering
## 3. Feature Selection
## 4. Model Building
## 5. Model Deployment

##..................................Data Analysis...................................
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns",None)
sns.set(rc={"figure.figsize":(12,8)})

data=pd.read_csv("train.csv")

## in the DATA ANALYSIS ,we will analysis to find out the below stuff..................

##1. Missing values
##2. All the numerical variables
##3. Distribution of the numerical variables
##4. Cardinality of categorical variables
##5. Outliers
##6. Relationship between independent and independent features 

