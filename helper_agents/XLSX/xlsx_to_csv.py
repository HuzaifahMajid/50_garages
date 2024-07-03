import pandas as pd
import os

def excel_to_csv(file_path, output_dir):
    # Read the entire Excel file
    xls = pd.ExcelFile(file_path)
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over each sheet name and save it as a CSV file
    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        # Sanitize sheet name for use as a file name
        sanitized_sheet_name = sheet_name.replace("/", "-").replace("\\", "-")
        output_file = os.path.join(output_dir, f"{sanitized_sheet_name}.csv")
        df.to_csv(output_file, index=False)
        print(f"Saved {sheet_name} to {output_file}")

def main():
    file_path = 'inspectionStatus.xlsx'  # Replace with your Excel file path
    output_dir = 'output_csv_files'     # Replace with your desired output directory
    
    # Convert Excel sheets to CSV files
    excel_to_csv(file_path, output_dir)

if __name__ == "__main__":
    main()
