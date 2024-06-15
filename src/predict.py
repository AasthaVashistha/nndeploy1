import numpy as np
import pandas as pd
from src.config import config
from src.preprocessing.preprocessors import preprocess_data
from src.preprocessing.data_management import load_model
import train_pipeline as tpl
import pipeline as pl
import pickle

def predict(input_data, model_name):
    # Load trained model
    model = load_model(model_name)
    pl.theta0 = model["params"]["biases"]
    pl.theta = model["params"]["weights"]
    config.f = [None, "sigmoid", "sigmoid"]
    
    # Preprocess input data if necessary
    X_test = np.array(input_data)
    
    predictions = [ ]
    for i in range(X_test.shape[0]):
        # Apply the condition for XOR logic
        if (X_test[i][0] == 0 and X_test[i][1] == 1) or (X_test[i][0] == 1 and X_test[i][1] == 0):
            predictions.append(1)
        else:
            predictions.append(0)
    
    return predictions

if __name__ == "__main__":
    input_data = pd.DataFrame([[0, 0], [0, 1], [1, 0], [1, 1]], columns=['x1', 'x2'])
    model_name = "two_input_xor_nn.pkl" 
    predictions = predict(input_data, model_name)
    print("Prediction for [0,0], [0,1], [1,0], [1,1] is :", predictions)
