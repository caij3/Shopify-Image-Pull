from get_properties import get_properties
from clean_csv import clean_csv
from merge_sheets import merge_files
import os

# Combines the previous files to remove manual process
# Order: clean, get_properties, merge

# Clean the CSV file
def run():
    folder_path = 'excel_files'

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):  # Check if it is a file
            print(file_name)

if __name__ == '__main__':
    run()