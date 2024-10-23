import numpy as np

# Create the grades array
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# Calculate mean, median, and standard deviation
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_deviation = np.std(grades)

# Find maximum and minimum grades
max_grade = np.max(grades)
min_grade = np.min(grades)

# Sort grades in ascending order
sorted_grades = np.sort(grades)

# Find the index of the highest grade
index_of_highest = np.argmax(grades)

# Count the number of students who scored above 90
count_above_90 = np.sum(grades > 90)

# Calculate the percentage of students who scored above 90
percentage_above_90 = np.mean(grades > 90) * 100

# Calculate the percentage of students who scored below 75
percentage_below_75 = np.mean(grades < 75) * 100

# Extract grades above 90
high_performers = grades[grades > 90]

# Create an array of passing grades (above 75)
passing_grades = grades[grades > 75]

# Print the results
print(f"Grades: {grades}")
print(f"Mean Grade: {mean_grade:.2f}")
print(f"Median Grade: {median_grade:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")
print(f"Maximum Grade: {max_grade}")
print(f"Minimum Grade: {min_grade}")
print(f"Sorted Grades: {sorted_grades}")
print(f"Index of Highest Grade: {index_of_highest}")
print(f"Number of Students Scoring Above 90: {count_above_90}")
print(f"Percentage of Students Scoring Above 90: {percentage_above_90:.2f}%")
print(f"Percentage of Students Scoring Below 75: {percentage_below_75:.2f}%")
print(f"High Performers (Grades Above 90): {high_performers}")
print(f"Passing Grades (Above 75): {passing_grades}")