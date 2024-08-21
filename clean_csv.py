import pandas as pd

# Load the CSV file into a dataframe
csv_file = pd.read_csv('products_export_1.csv')  # Replace with your actual CSV file name

# Step 1: Remove rows where "Image Src" is empty
csv_file_cleaned = csv_file[csv_file['Image Src'].notna()]

# Step 2: Group by "Handle" and fill missing "Vendor" values within the group
csv_file_cleaned['Vendor'] = csv_file_cleaned.groupby('Handle')['Vendor'].transform(lambda x: x.ffill().bfill())

# Step 3: Save the cleaned dataframe back to a CSV file
csv_file_cleaned.to_csv('cleaned_csv.csv', index=False)

print("done")
