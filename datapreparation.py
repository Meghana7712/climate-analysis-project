import pandas as pd

# Load the dataset
df = pd.read_csv("GlobalWeatherRepository.csv")

# Check missing values per column
print("Missing values per column:")
print(df.isnull().sum())

# Show total rows and columns
print("\nDataset shape (rows, columns):", df.shape)
# Save a cleaned copy
df.to_csv("CleanedWeatherRepository.csv", index=False)
print("\nCleaned dataset saved as CleanedWeatherRepository.csv")
