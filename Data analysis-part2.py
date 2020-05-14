##.........................................DATA ANALYSIS............................

##..................................[ Missing values ]...............................
data.shape

features_na=[features for features in data.columns if data[features].isnull().sum()>=1]
for i in features_na:
    print(i,np.round((data[i].isnull().sum()/len(data[i]))*100,4),"%")

##................Alternate method by the help of return method..........................

def missingvalues(num):
    result=[]
    for i in features_na:
        result.append(i)
    return(np.round((data[result].isnull().mean())*100,4))

a=missingvalues(features_na)

## ...........................Alternate method by the help of pandas.......................
b=data.isnull().sum()/len(data)*100
b=pd.DataFrame(b)
b.columns=["missing_values"]
c=b.loc[b["missing_values"]>0]
#.................................................................................................
## There are many missing values,we need to find the relationship between missing values and sales price.

data1=data.copy()

for j in features_na:
    data1[j]=np.where(data1[j].isnull(),1,0)
    data1.groupby(j)["SalePrice"].median().plot.bar(color=['red',"burlywood"])
    plt.title(j)
    plt.show()

## here the relationship b/w missing values and dependent variable are clearly visible.so we need to replace 
# these null values with something meaningful which we do in the feature engineering section.

#.........................Bifurcate numercial labels and categorical labels..............
    
num_features=[num for num in data.columns if data[num].dtypes != "O"]
num_data=data[num_features]

## ...................................Alternate method..................................
data_obj=data.select_dtypes( "O")
data_numa=data.drop(data_obj,axis=1)

##...................................TEMPORAL VARIABLE..................................

#--------- IN THE DATASET, WE HAVE 4 VARIABLES WHICH ARE COMING UNDER YEARS CATEGORY------
yr_feature=[k for k in num_features if "Yr" in k or "Year" in k]
yr__data=data[yr_feature]

for y in yr_feature:
    data.groupby(y)["SalePrice"].median().plot()
    plt.xlabel(y)
    plt.ylabel("SalePrice")
    plt.title("SalePrice vs {}".format(y))
    plt.show()
    
## HERE,WE WILL COMPARE THE DIFFERENCE BETWEEN ALL YEARS WITH SALESPRICE
data2=data.copy()
for f in yr_feature:
    if f!="YrSold":
        data2[f]=data2["YrSold"]-data2[f]
        plt.scatter(data2[f],data["SalePrice"])
        plt.xlabel(f)
        plt.ylabel("SalePrice")
        plt.show()

##--------------------Numerical features are usally of 2 types 1)continous 2) discrete-------------------
## -------------------to find out all the discrete variable amongst all the numerical variable--------------

discrete_feature=[d for d in num_features if len(data[d].unique())<25 and d not in yr_feature +["Id"] ]

discrete_data=data[discrete_feature]

data3=data.copy()
for q in discrete_feature:
    data3.groupby(q)["SalePrice"].median().plot.bar(color=["b","r","g","y","c","m","k","red","orange","green","blue","cyan","magenta","yellow"])
    plt.xlabel(q)
    plt.ylabel("SalePrice")
    plt.title(q)
    plt.show()
    
##........................continous variables..............................................

con_feature=[c for c in num_features if c not in discrete_feature + yr_feature +["Id"]]

for a in con_feature:
    data[a].hist(bins=25,color="green")
    plt.xlabel(a)
    plt.ylabel("count")
    plt.title(a)
    plt.show()






