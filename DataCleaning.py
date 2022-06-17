import numpy as np
import pandas as pd
import h5py
class cleaning:
    def __init__(self,value):
        self.df=value
   
    def clean(self):
        print(self.df)
        #check Null values
        self.df[self.df.Type.isnull()]
        #rows of the column Rating having NULL values
        self.df[self.df.Rating.isnull()]
        #replace null values in colum 'type' with keword "no-price"
        self.df['Type'].fillna("No price", inplace = True)
        self.df.isnull().sum()
        #replace null values in colum 'Content Rating' with keword "0"
        self.df[self.df['Content Rating'].isnull()]
        self.df.loc[10468:10477, :]
        #drop a row with missing value
        self.df.dropna(subset = ['Content Rating'], inplace=True)
        #removing unwanted colums
        self.df.drop(['Current Ver','Last Updated', 'Android Ver'], axis=1, inplace=True)
        print("printing header after removing colums")
        self.df.head()
        #replace the missing values of the Rating Column with the Mode value of that entire column.
        modeValueRating = self.df['Rating'].mode()
        modeValueRating[0]
        self.df['Rating'].fillna(value=modeValueRating[0], inplace = True)
        #Converting the Reviews column to integer
        self.df['Reviews'] = self.df.Reviews.astype(int)
        #Converting the Size Column from object to integer.
        self.df['Size'] = self.df.Size.apply(lambda x: x.strip('+'))# Removing the + Sign
        #Removing the , Symbol
        self.df['Size'] = self.df.Size.apply(lambda x: x.replace(',', ''))
        #Replacing the M by multiplying the value with 1000000
        self.df['Size'] = self.df.Size.apply(lambda x: x.replace('M', 'e+6'))# For converting the M to Mega
        #Replacing the k by multiplying the value with 1000.
        self.df['Size'] = self.df.Size.apply(lambda x: x.replace('k', 'e+3'))
        #Replacing the `Varies with device` value with *Nan*.
        self.df['Size'] = self.df.Size.replace('Varies with device', np.NaN)
        self.df.dropna(subset = ['Size'], inplace=True)
        #Converting the Installs column from object to integer
        self.df['Installs'] = self.df.Installs.apply(lambda x: x.strip('+'))
        #remove the , from the numbers.
        self.df['Installs'] = self.df.Installs.apply(lambda x: x.replace(',', ''))
        #convert it from string type to numeric type
        self.df['Installs'] = pd.to_numeric(self.df['Installs'])
        #Price column from objectto numeric
        self.df['Price'].value_counts()
        #remove the $ symbol from those values
        self.df['Price'] = self.df.Price.apply(lambda x: x.strip('$'))
        #convert the values to Numeric type.
        self.df['Price'] = pd.to_numeric(self.df['Price'])
        self.df.describe()
        #create hd5 file
        hf = h5py.File('C:\\Users\\Rabia\\Desktop\\202193590_project\\data\\data.h5', 'w')
        #hf.create_dataset('dataset_1', data=self.df)
        self.df.to_csv('data\\cleandata.csv', index=False)
        return self.df

        
   
        
    
        
        
    
    