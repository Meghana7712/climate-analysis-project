import pandas as pd
import os

# Step 1: Load dataset
input_file = "CleanedWeatherRepository.csv"  # Use your existing CSV
if not os.path.exists(input_file):
    print(f"❌ Error: {input_file} not found in the folder.")
    exit()

df = pd.read_csv(input_file)
print("✅ Dataset loaded successfully!\n")

# Step 2: Inspect dataset structure
print("Dataset structure:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Step 3: Identify missing values, anomalies, and data coverage
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nBasic statistics (numeric columns):")
print(df.describe())

# Step 4: Handling missing or inconsistent entries
# Example: Fill missing numeric values with mean
numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mean(), inplace=True)
        print(f"✅ Filled missing values in {col} with mean")

# Example: Fill missing categorical values with mode
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mode()[0], inplace=True)
        print(f"✅ Filled missing values in {col} with mode")

# Step 5: Convert units
# Convert Fahrenheit to Celsius if necessary
if 'temperature_fahrenheit' in df.columns:
    df['temperature_celsius'] = (df['temperature_fahrenheit'] - 32) * 5/9
    print("✅ Converted Fahrenheit to Celsius")

# Step 6: Normalize numeric values (0-1 scale)
for col in ['temperature_celsius', 'wind_kph']:
    if col in df.columns:
        df[col + "_normalized"] = df[col] / df[col].max()
        print(f"✅ Normalized column: {col}")

# Step 7: Aggregate or filter data
# Example: Keep only relevant columns
columns_to_keep = ['country', 'location_name']
for col in ['temperature_celsius', 'temperature_celsius_normalized', 'wind_kph', 'wind_kph_normalized']:
    if col in df.columns:
        columns_to_keep.append(col)
df = df[columns_to_keep]
print(f"\n✅ Columns after filtering: {columns_to_keep}")

# Optional: Example aggregation by country
if 'country' in df.columns:
    country_avg = df.groupby('country').mean(numeric_only=True).reset_index()
    country_avg.to_csv("Country_Averages.csv", index=False)
    print("✅ Aggregated data by country saved as 'Country_Averages.csv'")

# Step 8: Save final cleaned dataset
output_file = "CleanedWeatherRepository_Final.csv"
df.to_csv(output_file, index=False)
print(f"\n✅ Cleaned dataset saved as '{output_file}'")