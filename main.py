import csv

# Open the CSV file downloaded from AWS Cost Explorer
with open('costs.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row if it exists
    #next(csv_reader, None)

    service = next(csv_reader)
    cost = next(csv_reader)

service_output_file_path = 'zservice_list.csv'
cost_output_file_path = 'zcost_list.csv'

cleaned_service = [item.replace('($)', '') for item in service]

with open(service_output_file_path, mode='w', newline='') as service_csv:
    writer = csv.writer(service_csv)

    # Write the header row
    writer.writerow(['Service'])

    # Write each 'Service' item as a separate row
    for service_item in cleaned_service:
        writer.writerow([service_item])

print(f"'Service' list has been written to '{service_output_file_path}'.")

# Write the 'Cost' list to a CSV file
with open(cost_output_file_path, mode='w', newline='') as cost_csv:
    writer = csv.writer(cost_csv)

    # Write the header row
    writer.writerow(['Cost'])

    # Write each 'Cost' item as a separate row
    for cost_item in cost:
        writer.writerow([cost_item])

    print(f"'Cost' list has been written to '{cost_output_file_path}'.")