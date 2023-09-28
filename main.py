import csv
import pandas as pd

# Open the CSV file downloaded from AWS Cost Explorer
with open('costs.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    service = next(csv_reader)
    cost = next(csv_reader)

# Remove '($)' from 'Service' list items
cleaned_service = [''.join(char for char in item if char.isalnum() or char.isspace()) for item in service]
# Uses double-digit floats
converted_costs = []
for value in cost:
    try:
        float_value = float(value)
        formatted_value = "{:.2f}".format(float_value)
    except ValueError:
        input_string = value
        formatted_value = ''.join(char for char in input_string if char.isalnum() or char.isspace())
    converted_costs.append(formatted_value)

# Create a pandas DataFrame with 'Service' and 'Cost' columns
df = pd.DataFrame({'Service': cleaned_service, 'Cost': converted_costs})

# Define the output Excel file path
excel_output_file_path = 'structured_costs.xlsx'

# Write the DataFrame to an Excel file with 'Service' and 'Cost' columns
df.to_excel(excel_output_file_path, index=False)

print(f"Data has been written to '{excel_output_file_path}'.")
