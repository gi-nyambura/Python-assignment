# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting style
sns.set(style='whitegrid')

# Load dataset with error handling
try:
    df = pd.read_csv("clean_jobs.csv")
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    print("Error: File not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Task 1: Load and Explore the Dataset
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Clean missing values
df['work_type'].fillna('Unknown', inplace=True)
df['employment_type'].fillna('Unknown', inplace=True)

# Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe(include='all'))

# Group by company to count how many jobs each company posted
company_job_counts = df['company'].value_counts().head(10)
print("\nTop 10 Companies by Job Postings:")
print(company_job_counts)

# Group by location and count jobs
location_group = df['location'].value_counts().head(10)
print("\nTop 10 Locations by Job Availability:")
print(location_group)

# Convert date_posted to datetime
df['date_posted'] = pd.to_datetime(df['date_posted'], errors='coerce')

# Task 3: Data Visualization

# 1. Line chart: Job postings over time
jobs_per_day = df['date_posted'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
jobs_per_day.plot(kind='line', marker='o')
plt.title('Job Postings Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Postings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar chart: Top companies by number of job postings
plt.figure(figsize=(10, 6))
sns.barplot(x=company_job_counts.values, y=company_job_counts.index, palette='viridis')
plt.title('Top 10 Companies by Number of Job Postings')
plt.xlabel('Number of Job Postings')
plt.ylabel('Company')
plt.tight_layout()
plt.show()

# 3. Histogram: Frequency of job postings by work type
plt.figure(figsize=(8, 6))
sns.histplot(df['work_type'], bins=10, kde=False)
plt.title('Distribution of Work Types')
plt.xlabel('Work Type')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Scatter plot: Dummy plot (since no numerical columns exist for direct scatter)
# Simulate using job ID and employment_type (as an example)
df['id'] = pd.to_numeric(df['id'], errors='coerce')
plt.figure(figsize=(8, 6))
sns.scatterplot(x='id', y='employment_type', data=df, hue='company', legend=False)
plt.title('Job ID vs Employment Type')
plt.xlabel('Job ID')
plt.ylabel('Employment Type')
plt.tight_layout()
plt.show()

# Observations (to write in markdown or print in cell):
print("\nObservations:")
print("- Most job postings are clustered on recent dates (based on date_posted).")
print("- Meta is the top hiring company in this dataset.")
print("- There are several missing values in 'work_type' and 'employment_type', which were filled with 'Unknown'.")
print("- The dataset lacks strong numerical columns for statistical correlations.")
