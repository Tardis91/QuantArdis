import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import yfinance as yf
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.errors import SettingWithCopyWarning  # Import the warning class

# Ignore warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

# Set the seaborn theme
sns.set_theme(context="talk", style="whitegrid", palette="colorblind", color_codes=True, rc={"figure.figsize": [12, 8]})

# Download historical data for a stock (e.g., Apple)
symbol = "AAPL"
df = yf.download(symbol, start="2010-01-01", end="2019-12-31")
# Convert 'month' to ordered categorical so seaborn can interpret the x-axis correctly
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = pd.Categorical(df['date'].dt.strftime("%b"), categories=month_order, ordered=True)


df['Date'] = df.index
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.strftime("%b")

# Define month order and convert to categorical
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

# Now plot
sns.lineplot(data=df, x="month", y="Close", hue="year", style="year", legend="full", palette="colorblind")

# Plotting the stock data (Close Price) with seasonal variation per month
sns.lineplot(data=df, x="month", y="Close", hue="year", style="year", legend="full", palette="colorblind")

plt.title(f"{symbol} - Seasonal Plot of Closing Price")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
sns.despine()
plt.tight_layout()
# plt.savefig("images/figure_6_2", dpi=200)  # Uncomment to save the figure
plt.show()

print(df.columns)  # Or use st.write(df.columns) if you're in Streamlit
print(df.head())   # To inspect actual data
