import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import os.path

# Load the CSV file
df = pd.read_csv('products_export_2.csv')

# Prepare a list to store the results
results = []
lprio = 0
mprio = 0
hprio = 0

# Iterate through the rows of the DataFrame
for index, row in df.iterrows():
    if index == 20:  # Optional: Limit rows for testing
        break

    image_url = row['Image Src']
    title = row['Handle']
    pos = row['Image Position']

    if pd.isna(image_url) or image_url.strip() == '':
        continue

    try:
        # Fetch the image from the URL
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))

        # Get image dimensions
        width, height = img.size

        prio = ""

        # Check if either dimension is less than 600px
        if (width <= 700 and height <= 700):
            prio = "High"
            hprio += 1
        elif (width <= 750 and height <= 750):
            prio = "Medium"
            mprio += 1
        elif (width <= 750 or height <= 750):
            prio = "Low"
            lprio += 1

        if prio != "":
            result = {
                'Title': title,
                'Pic Num': pos,
                'Dimensions': f'{width}x{height}',
                'URL': image_url,
                'Priority': prio
            }
            results.append(result)
            # Print the result
            #print(f'Title: {title}\nPic Num: {pos}\nDimensions: {width}x{height}\nURL: {image_url}')
            #print("--------------------------------------------------------------")
            
    except Exception as e:
        continue
        #print(f'Failed to process image for link: {image_url}. Error: {e}')

print("Total: " + str(lprio + mprio + hprio))
print("High Priority: " + str(hprio))
print("Medium Priority: " + str(mprio))
print("Low Priority: " + str(lprio))

# Convert the results list to a DataFrame
results_df = pd.DataFrame(results)

# Path to the Excel file
excel_name = 'blurry_results'

# Initialize file name
i = 0
temp = excel_name
while os.path.isfile(f"{temp}.xlsx"):
    i += 1
    temp = f"{excel_name}_{i}"

# Final file name with extension
excel_file = f"{temp}.xlsx"

# Save the DataFrame to an Excel file
results_df.to_excel(excel_file, index=False)
