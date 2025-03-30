import pandas as pd
import numpy as np
import talib
import matplotlib.pyplot as plt

# Sample Data: Generate random closing prices
np.random.seed(42)
data = {'Close': np.random.normal(100, 2, 100)}  # Simulating 100 price points around 100
df = pd.DataFrame(data)

# Calculate Bollinger Bands (20-period moving average, 2 standard deviations)
df['Upper'], df['Middle'], df['Lower'] = talib.BBANDS(df['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)

# Plot the Bollinger Bands
plt.figure(figsize=(10, 5))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['Upper'], label='Upper Band', linestyle='dashed', color='red')
plt.plot(df['Middle'], label='Middle Band (SMA)', linestyle='dotted', color='green')
plt.plot(df['Lower'], label='Lower Band', linestyle='dashed', color='red')
plt.fill_between(df.index, df['Upper'], df['Lower'], color='gray', alpha=0.2)
plt.legend()
plt.title('Bollinger Bands')
plt.show()
