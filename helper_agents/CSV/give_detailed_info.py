import pandas as pd
import sys

def analyze_csv(file_path):
    """
    Analyze a CSV file and print out various statistics and information.

    This function reads the CSV file into a Pandas DataFrame, and then extracts
    various information about the data, such as basic information, summary statistics,
    column names, and the number of rows and columns.

    Parameters:
    file_path (str): The path to the CSV file to analyze.

    Returns:
    None
    """
    try:
        # Read the CSV file into a DataFrame
        # This may take some time for large files, so be patient!
        df = pd.read_csv(file_path)
        
        # Get basic information about the DataFrame
        # This includes the index dtype and column dtypes, non-nullable counts, and memory usage
        info = df.info()
        
        # Get summary statistics
        # This includes the count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum for each column
        summary_stats = df.describe()
        
        # Get column names
        # This is a list of strings, where each string is the name of a column
        columns = df.columns.tolist()
        
        # Get number of rows and columns
        # This is a tuple of two integers, where the first integer is the number of rows and the second integer is the number of columns
        num_rows, num_cols = df.shape
        
        # Display the results
        print(f"CSV File Analysis: {file_path}\n")
        print("1. Basic Information:")
        print(info)
        print("\n2. Summary Statistics:")
        print(summary_stats)
        print("\n3. Column Names:")
        print(columns)
        print(f"\n4. Number of Rows: {num_rows}")
        print(f"5. Number of Columns: {num_cols}")
    
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty. Please provide a non-empty CSV file.")
    except pd.errors.ParserError:
        print(f"Error: Unable to parse the file {file_path}. Please check the file format and try again.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist. Please provide a valid file path.")
    except pd.errors.DtypeWarning:
        print(f"Warning: The file {file_path} contains mixed data types. This may affect the accuracy of the analysis.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}. Please try again or contact the developer for assistance.")

def main():
    """
    Main entry point of the script.

    This function checks the command line arguments, and then calls the analyze_csv function
    to analyze the specified CSV file.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        print("Example: python script.py input.csv")
        sys.exit(1)
    
    # Get the file path from the command line arguments
    file_path = sys.argv[1]
    
    # Analyze the CSV file
    analyze_csv(file_path)

if __name__ == "__main__":
    main()