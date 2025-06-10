
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:34:34 2019

@author: sidhidatrinayak
"""

import pandas as pd
import numpy as np
from pandas import Series,DataFrame

data=Series(['one','two',np.nan,'four'])
data
#check if it has null values
data.isnull()
data.isna()
#how to handle missing values
data.dropna()
data.fillna(10)

#create a new dataframe

df=DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])
df

df.isnull()
df.dropna()
df.iloc[:,1].isnull()
#delete the rows that is having all missing value
df.dropna(how='all')
df.dropna()
#if you want to check if the column has missing values or not?
df
df.dropna(axis=1)

#define a variable for np.nan
npn=np.nan

df2=DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])
df2
#the row that is having at least 2 values will get printed
df2.dropna(thresh=2)
df2.dropna(thresh=2,axis=1)
#the row that is having at least 3 values will get printed
df2.dropna(thresh=3)


df
#how to fill the values 

df2.fillna(1)
df2.fillna(0)
df2
df2.fillna({0:1,1:2,2:3,3:4})
df2
df2.fillna(1,inplace=True)
df2
df2

dt=pd.read_csv('F:\\dataset\\loan_small.csv')
dt
dt.head(10)
dt.info()

#Get Missing Values
dt.isnull()
dt.isnull().sum(axis=0)

#handling Missing values
#drop the rows having missing values

cleandata=dt.dropna()
cleandata

dt
#drop the rows having missing values in perticular column
dt
cleandata=dt.dropna(subset=['Loan_Status'])
cleandata


dt1=dt.copy()  #copt of dataset in dt
dt1
cols=['Gender','Area','Loan_Status']
dt1[cols].mode()
dt1[cols].isnull().sum(axis=0)
#replace the missing values in the above three columns with their corresponding mode values

dt1[cols]=dt1[cols].fillna(dt1.mode().iloc[0])
dt1[cols]


dt1.mode()

#Replace the missing values in the columns having numerical values
dt1.columns
cols1=['ApplicantIncome','CoapplicantIncome','LoanAmount']
dt1[cols1]
dt1[cols1].isnull().sum()
dt1[cols1].mean()
dt1[cols1]=dt1[cols1].fillna(dt1[cols1].mean())
dt1[cols1]
dt1[cols1].isnull().sum(axis=0)


x=np.array([12,3,3,np.nan,np.nan,5,6,7,np.nan,6,7,8,9,npn,2,3,npn,npn,0])
d=pd.DataFrame(x)
d.ffill() #forward fill
d.bfill() #backword fill
#--------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
