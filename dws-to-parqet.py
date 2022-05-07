#!/usr/bin/python

import argparse, sys, os, csv

def main():
    input_file, output_file = get_files_from_arguments();
    input_data = get_data_from_input(input_file);
    write_data_to_output(input_data, output_file);

def get_files_from_arguments():
    argument_parser = argparse.ArgumentParser();

    argument_parser.add_argument('-i', '--input', dest='input', required=True, help='the input-file (CSV) which should be transformed (required)');
    argument_parser.add_argument('-o', '--output', dest='output', required=True, help='the output-file (CSV) to store the transformed data (required)');

    arguments = argument_parser.parse_args();

    input_file = arguments.input;
    output_file = arguments.output;

    if not input_file.endswith('.csv') or not output_file.endswith('.csv'):
        print('the input-file and output-file have to be a CSV-files!');
        sys.exit(2);

    if not os.path.exists(input_file):
        print(input_file, 'does not seem to exist!');
        sys.exit(2);

    if os.path.exists(output_file):
        print(output_file, 'already exists. Deleting it...');
        os.remove(output_file);

    return (input_file, output_file);

# the DWS transaction-overview has the following structure (as of 2022-05-07):
# date; type; portfolio; fonds-name; isin; shares; price per share; amount; currency
def get_data_from_input(input_file):
    with open(input_file, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';');

        # skip header...
        next(csv_reader);
        
        data = [];
        for row in csv_reader:
            entry = {};

            entry['date'] = row[0].strip();
            entry['type'] = row[1].strip();
            entry['isin'] = row[4].strip();
            entry['shares'] = row[5].strip();
            entry['price'] = row[6].strip();
            entry['currency'] = row[8].strip();

            data.append(entry);

    return data;

def write_data_to_output(data, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';');

        # header
        csv_writer.writerow(['broker', 'currency', 'date', 'fee', 'isin', 'price', 'shares', 'tax', 'type']);

        for entry in data:
            
            if entry['type'].startswith('Regelm. Kauf'):
                type = 'Buy';
            elif entry['type'].startswith('Kauf'):
                type = 'Buy';
            elif entry['type'].startswith('Gutschrift'):
                type = 'Dividend';
            elif entry['type'].startswith('Verkauf'):
                type = 'Sell';
            else:
                print('Error: Unable to convert DWS type', entry['type']);
                continue;

            csv_writer.writerow(['DWS', entry['currency'], entry['date'], 0, entry['isin'], entry['price'], entry['shares'], 0, type]);

if __name__ == '__main__':
    main();