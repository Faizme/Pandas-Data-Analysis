import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data into df
df = pd.read_csv("data.csv")

# Display first few rows
print(df.head())

# Get descriptive statistics
print(df.describe())

# Find missing values
mv = df.isnull().sum()
print("Missing values in each column:\n", mv)

# Find mean of the 'Age' column
avg = df["Age"].mean()
print("Average of Age:", avg)

# Count of unique values in 'Age' column
uv = df["Age"].nunique()
print("Unique values in Age:", uv)

# Filter employees in the Engineering department
eng_emp = df[df['Department'] == 'Engineering']
print(eng_emp)

# Highest paid employee
max_salary = df['Salary'].max()
max_salary_emp = df[df['Salary'] == max_salary]
print("Highest paid employee:\n", max_salary_emp)

# Minimum age
min_age = df["Age"].min()
print(df[df["Age"] == min_age])

# Count of employees in each department
dep_count = df['Department'].value_counts()
print("Number of employees in each department:\n", dep_count)

# Sorting employees by age
sort = df.sort_values(by='Age', ascending=True)
print("Employees sorted by age:\n", sort)

# Add Experience column
df['Experience'] = df['Age'].apply(lambda x: "Senior" if x >= 30 else "Junior")
print("Data with Experience column:\n", df)

# Pie chart for department distribution
plt.figure(figsize=(8, 6))
plt.pie(dep_count, labels=dep_count.index, autopct="%1.1f%%", startangle=140)
plt.title("Department Distribution")
plt.show()

# Histogram for Age Distribution
plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Histogram for Salary Distribution
plt.figure(figsize=(8, 6))
plt.hist(df['Salary'], bins=10, color='lightcoral', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Scatter plot for Age vs Salary
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Salary'], color='green', alpha=0.6)
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# Box plot for Salary by Department
plt.figure(figsize=(10, 6))
sns.boxplot(x='Department', y='Salary', data=df, palette='Set2')
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# Correlation Matrix
corr = df[['Age', 'Salary']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=1)
plt.title('Correlation Matrix')
plt.show()

# Group data by department
grouped = df.groupby('Department')[['Salary', 'Age']].mean()
print(grouped)

# Bar chart for average salary by department
plt.figure(figsize=(10, 6))
grouped['Salary'].plot(kind='bar', color='lightblue', edgecolor='black')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.show()

# Bar chart for average age by department
plt.figure(figsize=(10, 6))
grouped['Age'].plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Average Age by Department')
plt.xlabel('Department')
plt.ylabel('Average Age')
plt.xticks(rotation=45)
plt.show()
