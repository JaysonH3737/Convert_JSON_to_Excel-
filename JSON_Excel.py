import json

# first you must install xwlt using "pip install xlwt" command in Comand Prompt with eleveated privlages (Run As Administator) 
import xlwt

# Read the JSON file
# Replace "YOUR_FILE_NAME" with the name of your json file everywhere you see it
with open("YOUR_FILE_NAME.json ", "r") as json_file:
    YOUR_FILE_HERE_data = json.load(json_file)

# Create an Excel file
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("Sheet 1")

# Write the JSON data to the Excel file
for i, row in enumerate(json_data):
    for j, col in enumerate(row):
        worksheet.write(i, j, col)

# Save the Excel file
workbook.save("YOUR_FILE_NAME_database.xls")
