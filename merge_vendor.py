import pandas as pd

# Load the Excel file and the cleaned CSV file into dataframes
excel_file = pd.read_excel('blurry_results_1.xlsx')
cleaned_csv = pd.read_csv('cleaned_csv_1.csv')

# Merge the two dataframes on 'Title' from Excel and 'Handle' from CSV
merged_file = pd.merge(excel_file, cleaned_csv[['Handle', 'Vendor']], left_on='Title', right_on='Handle', how='left')

# Drop the 'Handle' column as it’s not needed anymore
merged_file.drop(columns=['Handle'], inplace=True)

# Drop duplicate rows based on 'Title', keeping the first occurrence
merged_file.drop_duplicates(subset=['URL'], keep='first', inplace=True)

# Reorder the columns to place 'Vendor' first
columns_order = ['Vendor'] + [col for col in merged_file.columns if col != 'Vendor']
merged_file = merged_file[columns_order]

# Save the resulting dataframe back to an Excel file
merged_file.to_excel('modified_file_1.xlsx', index=False)

print("done")
