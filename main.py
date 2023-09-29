import csv
import pandas as pd
import argparse
import os

def read_user_cli_args():
    parser = argparse.ArgumentParser(
        prog='pregs',
        description="pregs is a lame shorthand word for 'lazy' in Portuguese. It converts a CSV file into a XLSx spreadsheet (one-way only), allowing simple copy/paste.",
        epilog="Thanks for using Pregs and stay lazy!"
    )

    parser.add_argument(
        "convert", nargs="?", type=str, default='costs.csv', help="Enter the name of the CSV file that should be converted. Defaults to 'costs.csv' if not defined."
    )
    parser.add_argument(
        "clear", nargs="?", type=str, default='structured_costs.xlsx', help="Enter the name of the XLSx file that should be removed from app directory. Defaults to 'structured_costs.csv' if not defined."
    )
    parser.add_argument(
        "-o",
        "--output-file",
        nargs="?",
        default='structured_costs.xlsx',
        help="Defines the name of the output file. Defaults to 'structured_costs.xlsx'",
    )
    return parser.parse_args()

def store_csv_lines(csv_file_name):
    # Open the CSV file downloaded from AWS Cost Explorer
    with open(csv_file_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        service = next(csv_reader)
        cost = next(csv_reader)
    return service, cost

def format_stored_values(service, cost):
    # Remove 'symbols' from 'Service' list items
    cleaned_service = [''.join(char for char in item if char.isalnum() or char.isspace()) for item in service]
    # Displays only double-digit floats
    converted_costs = []
    for value in cost:
        try:
            float_value = float(value)
            formatted_value = "{:.2f}".format(float_value)
        except ValueError:
            input_string = value
            formatted_value = ''.join(char for char in input_string if char.isalnum() or char.isspace())
        converted_costs.append('$' + formatted_value)
    return cleaned_service, converted_costs

def convert_into_xlsx(cleaned_service, converted_costs, excel_output_file_name):
    # Create a pandas DataFrame with 'Service' and 'Cost' columns
    df = pd.DataFrame({'Service': cleaned_service, 'Cost': converted_costs})

    # Write the DataFrame to an Excel file with 'Service' and 'Cost' columns
    df.to_excel(excel_output_file_name, index=False)

    print(f"Data has been written to '{excel_output_file_name}'.")


def delete_file(file_name):
    """Delete a file with the given name."""
    try:
        os.remove(file_name)
        print(f"'{file_name}' has been deleted.")
    except OSError as e:
        print(f"Error: {e}. Is the file open in another program?")


def main():
    user_args = read_user_cli_args()
    if user_args.convert:
        service, cost = store_csv_lines(user_args.convert)
        cleaned_service, converted_costs = format_stored_values(service, cost)
        convert_into_xlsx(cleaned_service, converted_costs, user_args.output_file)
    if user_args.clear:
        delete_file(user_args.clear)

if __name__ == "__main__":
    main()

