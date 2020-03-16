import pandas as pd
import numpy as np

# Data
bank_df = pd.read_csv("Data/bank.csv")

# Changing column names to be more suitable
bank_df.columns = bank_df.columns.str.replace(' ', '_')

# Dropping missing values
bank_df.dropna(inplace=True)
