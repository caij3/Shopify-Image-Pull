import pandas as pd

# Load the two Excel files into dataframes
def merge_files(files,output):
    for i in range(len(files)):
        df = pd.read_excel(files[i])
        if i == 0:
            combined_df = df
        else:
            combined_df = pd.concat([combined_df, df], ignore_index=True)
    combined_df.to_excel(output, index=False)
    print("Files combined and saved as 'combined_file.xlsx'.")
    return combined_df
