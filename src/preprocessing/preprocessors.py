import numpy as np
import os

from src.config import config 

class preprocess_data:

    # Creating a blueprint of the object to which the object will belong to 
    def fit(self,X,y-None):

        self.num_rows = X.shape[0]

        if len(X.shape) == 1:
             self.num_input_features = 1

        else:
                  self.num_rows = X.shape[1]

        if len(y.shape) == 1:
             self.target_feature_dim = 1
        else :
             self.target_feature_dim = y.shape[1]

    def transform(self,X=None,y=None):

           self.X = np.aaray(X).reshape(self.num_rows,self.num_input_features)
           self.Y = np.array(y).reshape(self.num_rows,self.target_feature_dim)

           return self.X, self.Y