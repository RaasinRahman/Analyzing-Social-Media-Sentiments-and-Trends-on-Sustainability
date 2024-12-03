import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#  sample data
np.random.seed(42)  
dates = pd.date_range(start='2024-11-01', periods=7, freq='D')
sentiments = np.random.uniform(low=-1.0, high=1.0, size=len(dates))

#  DataFrame
data = pd.DataFrame({'Date': dates, 'Sentiment': sentiments})

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Sentiment'], marker='o', linestyle='-')
plt.title('Sentiment Analysis of Tweets on Climate Change')
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.axhline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.show()
