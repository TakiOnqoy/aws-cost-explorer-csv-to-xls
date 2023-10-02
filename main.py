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
        "convert", nargs="?", type=str, help="Enter the name of the CSV file that should be converted."
    )
    parser.add_argument(
        "clear", nargs="?", type=str, help="Enter the name of the XLSx file that should be removed from app directory."
    )
    parser.add_argument(
        "-d",
        "--default",
        action="store_true",
        help="Set the name of files to default values: 'cost.csv' for input file and 'structured_costs.xlsx' to output file",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        nargs="?",
        help="Defines the name of the output file.",
    )
    return parser.parse_args()

def set_input_file_name(input_file_name, default=False):
    if default:
        input_file_name = 'costs.csv'
    return input_file_name
def set_output_file_name(output_file_name, default=False):
    if default:
        output_file_name = 'structured_costs.xlsx'
    return output_file_name

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
            converted_costs.append('$' + formatted_value)
        except ValueError:
            input_string = value
            formatted_value = ''.join(char for char in input_string if char.isalnum() or char.isspace())
            converted_costs.append(formatted_value)

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
        print(f"Error: {e}.")


def main():
    user_args = read_user_cli_args()
    input_file_name = set_input_file_name(user_args.convert, user_args.default)
    output_file_name = set_output_file_name(user_args.clear, user_args.default)
    if user_args.convert:
        service, cost = store_csv_lines(input_file_name)
        cleaned_service, converted_costs = format_stored_values(service, cost)
        convert_into_xlsx(cleaned_service, converted_costs, output_file_name)
    if user_args.clear:
        delete_file(output_file_name)

if __name__ == "__main__":
    main()

