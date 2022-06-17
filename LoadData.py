import numpy as np
import pandas as pd
class ReadData:
    def __init__(self,file):
        self.playstore_df=pd.read_csv(file)
    def show(self):
        self.playstore_df.head(5)
        self.playstore_df.info()
        
        rows = self.playstore_df.shape[0]
        column = self.playstore_df.shape[1]
        print('There are {} Rows and {} Columns in the dataset'.format(rows, column))
        self.playstore_df.columns
        self.playstore_df.isnull().sum()
        self.playstore_df.head()
      
    def raw_info(self):
        
        return self.playstore_df.info()
    def df(self):
       
        return self.playstore_df
   