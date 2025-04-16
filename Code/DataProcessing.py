# Adis Mahmic
# Dr. Price
# 04/12/2025
# Data Intensive Fundamentals

# Description:
# DataProcessing.py uses the pandas framework to read our reduced dataset and then replaces empty values within our two columns ("CONTRIBUTING FACTOR VEHICLE 1", and "CONTRIBUTING FACTOR VEHICLE 2")
# and replaces them with the replacement value "Unspecified". If needed un-comment line 23 (print(df.head(10)) to print the first 10 rows of the dataset to see if the code works.
# The changes are then saved to a new csv file called "Motor_Crash_Collisions_InitialData_cleaned.csv".

import pandas as pd

replacement_value = "Unspecified"
column_name = "CONTRIBUTING FACTOR VEHICLE 2"
column_name2 = "CONTRIBUTING FACTOR VEHICLE 1"
df = pd.read_csv("Motor_Crash_Collisions_InitialData.csv")

# Replace NaN and empty strings with "Unspecified"
df[[column_name, column_name2]] = df[[column_name, column_name2]].replace(
    to_replace=["", pd.NA, None, float('nan')], value=replacement_value
)
df[[column_name, column_name2]] = df[[column_name, column_name2]].fillna(replacement_value)

# print(df.head(10))

# Save it back to CSV if needed:
df.to_csv('Motor_Crash_Collisions_InitialData_cleaned.csv', index=False)
