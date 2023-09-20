import csv
import pandas as pd

# Open the CSV file downloaded from AWS Cost Explorer
with open('costs.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    service = next(csv_reader)
    cost = next(csv_reader)

# Remove '($)' from 'Service' list items
cleaned_service = [item.replace('($)', '') for item in service]

# Create a pandas DataFrame with 'Service' and 'Cost' columns
df = pd.DataFrame({'Service': cleaned_service, 'Cost': cost})

# Define the output Excel file path
excel_output_file_path = 'structured_costs.xlsx'

# Write the DataFrame to an Excel file with 'Service' and 'Cost' columns
df.to_excel(excel_output_file_path, index=False)

print(f"Data has been written to '{excel_output_file_path}'.")