import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.cross_validation import train_test_split
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

class trainingData:
    def __init__(self,data):
        self.df=data
    def trainModels(self):
        print(self.df)
    #for evaluation of error term and 
    def Evaluationmatrix(y_true, y_predict):
        print ('Mean Squared Error: '+ str(metrics.mean_squared_error(y_true,y_predict)))
        print ('Mean absolute Error: '+ str(metrics.mean_absolute_error(y_true,y_predict)))
        print ('Mean squared Log Error: '+ str(metrics.mean_squared_log_error(y_true,y_predict)))
    #to add into results_index for evaluation of error term 
    def Evaluationmatrix_dict(y_true, y_predict, name = 'Linear - Integer'):
        dict_matrix = {}
        dict_matrix['Series Name'] = name
        dict_matrix['Mean Squared Error'] = metrics.mean_squared_error(y_true,y_predict)
        dict_matrix['Mean Absolute Error'] = metrics.mean_absolute_error(y_true,y_predict)
        dict_matrix['Mean Squared Log Error'] = metrics.mean_squared_log_error(y_true,y_predict)
        return dict_matrix
    
    def RegressionEncoding(self):
    #Integer encoding
        X = self.df.drop(labels = ['Category','Rating','Genres','Genres_c'],axis = 1)
        y = self.df.Rating
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
        model = LinearRegression()
        model.fit(X_train,y_train)
        Results = model.predict(X_test)

        #Creation of results dataframe and addition of first entry
        resultsdf = pd.DataFrame()
        resultsdf = resultsdf.from_dict(Evaluationmatrix_dict(y_test,Results),orient = 'index')
        resultsdf = resultsdf.transpose()
        #dummy encoding

        X_d = df2.drop(labels = ['Rating','Genres','Category_c','Genres_c'],axis = 1)
        y_d = df2.Rating
        X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(X_d, y_d, test_size=0.30)
        model_d = LinearRegression()
        model_d.fit(X_train_d,y_train_d)
        Results_d = model_d.predict(X_test_d)

        #adding results into results dataframe
        resultsdf = resultsdf.append(Evaluationmatrix_dict(y_test_d,Results_d, name = 'Linear - Dummy'),ignore_index = True)
        plt.figure(figsize=(12,7))
        sns.regplot(Results,y_test,color='teal', label = 'Integer', marker = 'x')
        sns.regplot(Results_d,y_test_d,color='orange',label = 'Dummy')
        plt.legend()
        plt.title('Linear model - Excluding Genres')
        plt.xlabel('Predicted Ratings')
        plt.ylabel('Actual Ratings')
        plt.show()