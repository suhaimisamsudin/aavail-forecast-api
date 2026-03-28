# test endpoint - 26.03.2026 Suhaimi
# not fully working. need to debug further

import joblib
import pandas as pd

MODEL_PATH = 'model/forecast_model.pkl'

def predict_revenue(country, date):
    model = joblib.load(MODEL_PATH)
    
    # Transform country and date into feature vector
    # This is a placeholder — customize based on your features
    X_new = pd.DataFrame([{'feature1': 1, 'feature2': 2}])
    
    prediction = model.predict(X_new)[0]
    return prediction



