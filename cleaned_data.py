


import pandas as pd
import re

# Prompt the user for the file path with error handling
while True:
    try:
        file_path = input("Please enter the file path for the customer list CSV file: ")
        # Using 'with' to ensure the file is closed after reading
        with open(file_path, 'r') :
            customer_df = pd.read_csv(file_path, delimiter='|')
        break  # Exit the loop if the file is successfully loaded
    except FileNotFoundError:
        print("Error: The file was not found. Please check the path and try again.")

# Display the first few rows of the data if successfully loaded
print("Preview of Customer Data:")
print(customer_df.head())
print("\nData Info:")
print(customer_df.info())



# Use str.replace to clean the 'name' column directly
customer_df['name'] = customer_df['name'].str.replace(r"[^a-zA-Z\-. ]", "", regex=True)

# Display the cleaned 'name' column to check results
print("Cleaned Name Field:")
print(customer_df['name'].head())


# Define a function to clean and standardize phone numbers
def standardize_phone(phone):
    # Remove any non-digit characters
    digits = re.sub(r"\D", "", str(phone))
    
    # Check if the number has exactly 10 digits
    if len(digits) == 10:
        # Format as NNN-NNN-NNNN
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    else:
        return "Invalid"  # Mark as "Invalid" if not exactly 10 digits

# Apply the function to the 'phone' column
customer_df['phone'] = customer_df['phone'].apply(standardize_phone)

# Display the cleaned 'phone' column to check results
print("Standardized Phone Numbers:")
print(customer_df['phone'].head())

print(customer_df['sms-opt-out'].head(302))
# Fill missing values in 'sms-opt-out' with 'N' (opt-in)
customer_df['sms-opt-out'] = customer_df['sms-opt-out'].fillna('N')

# Display the 'sms-opt-out' column to check results
print("Updated SMS Opt-Out Field:")
print(customer_df['sms-opt-out'].head(302))


# Specify the output file name
clean_customer_data = "cleaned_customer_list.csv"

# Save the cleaned data to a CSV file
customer_df.to_csv(clean_customer_data, index=False)

# Print a confirmation message
print(f"Saved cleaned data to {clean_customer_data}")
