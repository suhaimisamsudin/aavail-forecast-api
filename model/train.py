# test endpoint - 26.03.2026 Suhaimi
# not fully working. need to debug further

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os
import glob

MODEL_PATH = 'model/forecast_model.pkl'

def train_model(data_dir='data/'):
    all_files = glob.glob(os.path.join(data_dir, "*.csv"))
    df_list = [pd.read_csv(f) for f in all_files]
    df = pd.concat(df_list)

    # Example: Simple regression
    X = df[['feature1', 'feature2']]  # Replace with your features
    y = df['target']                  # Replace with your target

    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print("Model trained and saved.")


