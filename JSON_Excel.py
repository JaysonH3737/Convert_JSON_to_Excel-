import json
import xlwt

# Read the JSON file
with open("vehicle_data.json", "r") as json_file:
    vehicle_data = json.load(json_file)

# Create an Excel file
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("Sheet 1")

# Write the JSON data to the Excel file
for i, row in enumerate(json_data):
    for j, col in enumerate(row):
        worksheet.write(i, j, col)

# Save the Excel file
workbook.save("vehicle_database.xls")
