import pandas as pd

# Load the two Excel files into dataframes
df1 = pd.read_excel('modified_file_1.xlsx')  # Replace with your first Excel file name
df2 = pd.read_excel('modified_file_2.xlsx')  # Replace with your second Excel file name

# Concatenate the two dataframes
combined_df = pd.concat([df1, df2], ignore_index=True)

# Optional: Drop duplicate rows if needed
# combined_df.drop_duplicates(inplace=True)

# Save the combined dataframe back to a new Excel file
combined_df.to_excel('combined_file.xlsx', index=False)

print("Files combined and saved as 'combined_file.xlsx'.")
