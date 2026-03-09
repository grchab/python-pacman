import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# -------------------------
# Data Generation
# -------------------------
# Suppose we have 2 years of daily data (approx. 500 trading days)
n_days = 500
days = np.arange(n_days)

# Simulate a baseline gold price trend
# Start at 1500 USD/oz and add a slight upward trend
baseline = 1500 + 0.1 * days

# Random noise
noise = np.random.normal(0, 10, size=n_days)

# Generate a binary geopolitical event variable
# Let's say events happen sporadically
# We'll randomly pick about 10% of days to be "event" days
event_days = np.zeros(n_days)
event_indices = np.random.choice(n_days, size=int(0.1*n_days), replace=False)
event_days[event_indices] = 1

# Increase gold price on event days by some amount (e.g., $20)
gold_price = baseline + noise + 20 * event_days

# Create a DataFrame
df = pd.DataFrame({
    'Day': days,
    'GoldPrice': gold_price,
    'GeopoliticalEvent': event_days
})

# -------------------------
# Modeling using ESL concepts
# -------------------------
# We'll do a simple linear regression: GoldPrice ~ 1 + GeopoliticalEvent

X = df[['GeopoliticalEvent']]  # predictor
y = df['GoldPrice']            # response

# Fit with sklearn
model = LinearRegression()
model.fit(X, y)

# Print coefficients
# Intercept is model.intercept_, coefficient for event is model.coef_[0]
print("Sklearn Linear Regression Results:")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficient for GeopoliticalEvent: {model.coef_[0]:.2f}")

# For more detailed statistical output, use statsmodels
X_sm = sm.add_constant(X)
ols_model = sm.OLS(y, X_sm).fit()
print("\nStatsmodels OLS Results:")
print(ols_model.summary())

# -------------------------
# Visualization
# -------------------------
sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Day', y='GoldPrice', hue='GeopoliticalEvent', data=df, palette=['blue', 'red'])
plt.title('Gold Price Over Time with Geopolitical Events')
plt.xlabel('Day')
plt.ylabel('Gold Price (USD/oz)')
plt.show()

# -------------------------
# Interpretation:
# -------------------------
# The coefficient for GeopoliticalEvent should be close to +20 in our synthetic data,
# indicating that on average, gold prices are about $20 higher when a geopolitical event occurs.
