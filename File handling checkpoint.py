# Import numpy library
import numpy as np

try:
    # Using with statement (context manager) which automatically closes the file
    # open the csv file and read the content of the file
    with open('Loan_prediction_dataset.csv', 'r') as file:
        data = file.readlines()
        
        # Remove the header (first row)
        header = data[0]
        loan_data = data[1:]
        
        # Create a list to store loan amounts
        loan_amounts = []
        
        # Extract loan amounts from each line
        for line in loan_data:
            values = line.strip().split(',')
            if len(values) >= 9:
                try:
                    loan_amount = float(values[8])
                    loan_amounts.append(loan_amount)
                except ValueError:
                    continue
        
        # Convert list to numpy array
        loan_amounts = np.array(loan_amounts)
        
        # Perform statistical analysis
        print("\nBasic Statistics:")
        print(f"Number of loans: {len(loan_amounts)}")
        print(f"Mean loan amount: {np.mean(loan_amounts):.2f}")
        print(f"Median loan amount: {np.median(loan_amounts):.2f}")
        print(f"Standard deviation: {np.std(loan_amounts):.2f}")
    
    print("\nFile has been closed automatically by the context manager.")

except FileNotFoundError:
    print("Error: The file 'loan_data.csv' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    