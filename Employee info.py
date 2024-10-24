import pandas as pd
# Create DataFrame

data = {'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'], 
        'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'], 
        'Age': [30, 40, 25, 35, 45, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'], 
        'Salary': [50000, 60000, 45000, 55000, 70000, 55000], 
        'Experience': [3, 7, 2, 5, 10, 4]}

employee_df = pd.DataFrame(data)

# Using iloc to select the first 3 rows
first_3rows = employee_df.iloc[:3]
print("First 3 rows:")
print(first_3rows)

# Using loc to select all rows where the Department is marketing
Dept_marketing = employee_df.loc[employee_df['Department'] == 'Marketing']
print("\nRows where Department is 'Marketing':")
print(Dept_marketing)

# Using iloc to select the Age and Gender columns for the first 4 rows
age_gender_first_4rows = employee_df.iloc[:4, [2, 3]]  # Age is column 2, Gender is column 3
print("\nAge and Gender for the first 4 rows:")
print(age_gender_first_4rows)

# Using loc to select the Salary and Experience columns for all rows where Gender is "Male"
male_salary_experience = employee_df.loc[employee_df['Gender'] == 'Male', ['Salary', 'Experience']]
print("\nSalary and Experience for rows where Gender is 'Male':")
print(male_salary_experience)
