import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv'
data_url = 'survey_data.csv'
df = pd.read_csv(data_url)
#print(df.info())

'''
# Instead .... (not showing all columns), show all columns
pd.set_option('display.max_columns', None)
print(df.head())
'''

# Print one column per line (fetching only column names)

# columns=df.columns
# for col in columns:
#     print(col)
# print()
# print("Total number of columns: ",len(columns))

print()
# Handling missing data - Checking missing values
print(df[['Employment', 'JobSat', 'RemoteWork']].isnull().sum())
df['Employment'] = df['Employment'].fillna(df['Employment'].mode()[0])
df['JobSat'] = df['JobSat'].fillna(df['JobSat'].mode()[0])
df['RemoteWork'] = df['RemoteWork'].fillna(df['RemoteWork'].mode()[0])
print()
print(df[['Employment', 'JobSat', 'RemoteWork']].isnull().sum())

# Analysing Experience vs job satisfaction
# Does more experience lead to higher job satisfaction?

# Convert YearsCodePro columng to Numeric
df['YearsCodePro'] = pd.to_numeric(df['YearsCodePro'], errors='coerce')
print()
bins = [0, 5, 10, 20, 50]
labels = ['0–5', '5–10', '10–20', '20+']
# Arranging value in labels
df['ExperienceRange'] = pd.cut(df['YearsCodePro'], bins=bins, labels=labels)
# Calculate Median Job Satisfaction per Range
median_jobsat = df.groupby('ExperienceRange', observed=True)['JobSat'].median()

print(median_jobsat)

# Visualize the Relationship

median_jobsat.plot(kind='bar')
plt.title('Median Job Satisfaction by Experience')
plt.xlabel('Experience Range (Years)')
plt.ylabel('Median Job Satisfaction')
plt.show()

# Count Plot for Job Satisfaction
sns.countplot(x='JobSat', data=df)
plt.title('Job Satisfaction Distribution')
plt.xlabel('Job Satisfaction')
plt.ylabel('Count')
plt.show()

# Remote Work Preferences by Job Role
# Remote Work Distribution
sns.countplot(x='RemoteWork', data=df)
plt.title('Remote Work Distribution')
plt.show()

remote_employment = pd.crosstab(df['Employment'], df['RemoteWork'])
print(remote_employment)

# # Visualize cross-tabulation
# remote_employment.plot(kind='bar', stacked=True)
# plt.title('Remote Work by Employment Type')
# plt.xlabel('Employment Type')
# plt.ylabel('Count')
# plt.show()

# finding the correct names of the country.
print(df['Country'].value_counts().head(10))
# removing the extra spaces from Country column
df['Country'] = df['Country'].str.strip()

# making a new table with filtered records only United States
#  usa_data = df[df['Country'] == 'United States of America']
usa_data = df[df['Country'].str.contains('United States', na=False)]
# drop values with NaN
languages = (
    usa_data['LanguageHaveWorkedWith']
    .dropna()
    .str.split(';')
    .explode()
)

top_languages = languages.value_counts().head(10)
# Listing the sum of each language
print(top_languages)

if not top_languages.empty:
    top_languages.plot(kind='bar', figsize=(10,5))
    plt.title('Top Programming Languages in the USA')
    plt.xlabel('Language')
    plt.ylabel('Count')
    plt.show()
else:
    print("No data available to plot.")

# Correlation between Experience and Satisfaction
sns.scatterplot(
    x='YearsCodePro',
    y='JobSatPoints_1',
    data=df
)
plt.title('Experience vs Job Satisfaction Score')
plt.xlabel('Years of Professional Coding')
plt.ylabel('Job Satisfaction Score')
plt.show()

# Education vs Employment Type
edu_emp = pd.crosstab(df['EdLevel'], df['Employment'])
print(edu_emp)
# Heatmap Visualization
sns.heatmap(edu_emp, annot=True, fmt='d', cmap='Blues')
plt.title('Education Level vs Employment Type')
plt.show()

# Save the Final Dataset
df.to_csv('survey_data_eda.csv', index=False)












