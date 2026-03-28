# test endpoint - 26.03.2026 Suhaimi
# not fully working. need to debug further

import pandas as pd
import matplotlib.pyplot as plt

def analyze_predictions(pred_file='logs/predictions.csv', actual_file='data/actual.csv'):
    preds = pd.read_csv(pred_file)
    actuals = pd.read_csv(actual_file)

    merged = preds.merge(actuals, on=['date', 'country'])
    merged['error'] = merged['forecast'] - merged['target']

    plt.plot(merged['date'], merged['forecast'], label='Forecast')
    plt.plot(merged['date'], merged['target'], label='Actual')
    plt.legend()
    plt.show()


