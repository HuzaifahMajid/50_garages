import csv

# Define the input and output file names
input_file = 'input.csv'
output_file = 'output.csv'

# Read the input CSV file
with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    
    # Get the fieldnames from the reader object and insert the new field
    fieldnames = reader.fieldnames
    index = fieldnames.index('FormattedAddress') + 1
    fieldnames.insert(index, 'ID Obtained')

    # Write to the output CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Add the new column and clear values after 'FormattedAddress'
            row['ID Obtained'] = ''
            for field in fieldnames[index + 1:]:
                row[field] = ''
            writer.writerow(row)

print(f"File '{output_file}' created successfully.")
