import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import os

def draw_plot():
    # Read data from file
    df = pd.read_csv(r'C:\Users\user\Desktop\PYTHON\Sea_level_Predictor\epa-sea-level.csv')

    # Ensure output directory exists
    output_dir = os.path.join(os.path.dirname(__file__), 'output2')
    os.makedirs(output_dir, exist_ok=True)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Sea Level Data')

    # Calculate first line of best fit (all years)
    res = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = np.arange(1880, 2051)
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line 1880-2013')

    # Calculate second line of best fit (from year 2000)
    recent_df = df[df['Year'] >= 2000]
    res_recent = stats.linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    x_pred_recent = np.arange(2000, 2051)
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, 'green', label='Best Fit Line 2000-2013')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)

    # Save plot and return data for testing
    plt.savefig(os.path.join(output_dir, 'sea_level_plot.png'))
    return plt.gca()

# For testing
if __name__ == '__main__':
    draw_plot()