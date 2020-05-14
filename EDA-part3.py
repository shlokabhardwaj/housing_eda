##--------------------------------EXPLORATORY DATA ANALYSIS-----------------------
import numpy as np
data4=data.copy()
for i in con_feature:
    if 0 in data4[i].unique():
        pass
    else:
        data4[i]=np.log(data[i])
        data4["SalePrice"]=np.log(data4["SalePrice"])
        plt.scatter(data4[i],data4["SalePrice"])
        plt.xlabel(i)
        plt.ylabel("SalePrice")
        plt.title(i)
        plt.show()
    
##-------------------------------OUTLIERS-------------------------------------------------
data5=data.copy()
for i in con_feature:
    if 0 in data[i].unique():
        pass
    else:
        data5[i]=np.log(data5[i])
        data5.boxplot(column=i)
        plt.ylabel(i)
        plt.title(i)
        plt.show()
##--------------------------------------CATEGORICAL FEATURES-------------------------
categorical_feature=[i for i in data.columns if data[i].dtypes=="O"]
data[categorical_feature].head()   

##-------TACKLE CARDINALITY(HOW MANY CATEGORIES HAVE IN A CATEGORY feature)---
data[categorical_feature].nunique()

#----Firstly determining the relation between categories of categorical variable and dependent variable-----
data6=data.copy()
for i in categorical_feature:
    data5.groupby(i)["SalePrice"].median().plot.bar(color=["b","r","g","y","c","m","k","red","orange","green","blue","cyan","magenta","yellow"])
    plt.xlabel(i)
    plt.ylabel("SalePrice")
    plt.title(i)
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    