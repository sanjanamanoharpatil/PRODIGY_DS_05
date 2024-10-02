import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'traffic accidents/accident data.csv'
accident_data = pd.read_csv(file_path)

# Convert 'Accident Date' to datetime
accident_data['Accident Date'] = pd.to_datetime(accident_data['Accident Date'], errors='coerce')

# Drop rows with missing values in key columns
cleaned_data = accident_data.dropna(subset=['Latitude', 'Longitude', 'Road_Surface_Conditions', 'Weather_Conditions'])

# Plot the distribution of accidents based on road surface conditions and weather conditions
plt.figure(figsize=(12, 6))
sns.countplot(data=cleaned_data, x='Road_Surface_Conditions', hue='Weather_Conditions')
plt.title('Accidents by Road Surface and Weather Conditions')
plt.xticks(rotation=45)
plt.show()

# Plot accident hotspots based on Latitude and Longitude using a scatter plot
plt.figure(figsize=(8, 8))
plt.scatter(cleaned_data['Longitude'], cleaned_data['Latitude'], c='red', alpha=0.5, s=10)
plt.title('Accident Hotspots by Location (Longitude vs Latitude)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
