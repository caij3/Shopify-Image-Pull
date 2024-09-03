from get_properties import get_properties
from clean_csv import clean_csv
from merge_sheets import merge_files
import os
from pathlib import Path

def run():
    folder_path = 'excel_files'
    cleaned = []
    files = []

    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            file_stem = Path(file_name).stem
            cleaned_output = file_stem + '_cleaned.csv'
            print(f"Cleaning {file_path} to {cleaned_output}")
            
            clean_csv(file_path, cleaned_output)
            cleaned.append(cleaned_output)

    for file in cleaned:
        properties_output = file.replace('.csv', '_properties')
        print(f"Getting properties for {file} into {properties_output}")
        
        excel_file = get_properties(file, properties_output, True)
        files.append(excel_file)

    # Ensure the generated files exist before attempting to merge
    # for file in files:
    #     if not os.path.exists(file):
    #         print(f"Error: Expected file '{file}' does not exist.")
    #         return

    merge_files(files, 'final_output.xlsx')
    print('Process completed successfully.')

if __name__ == '__main__':
    run()
