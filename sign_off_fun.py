import openpyxl
import pandas as pd
import sys
import SharePy

server_url = 'https://ts.accenture.com/'
site_url = server_url + "/sites/COOpsTeamLeads/"
opener = basic_auth_opener(server_url, "username", "password")

for sp_list in site.lists:
    print(sp_list.meta['Title'])

# file_path = r"C:\Users\illia.shaban.DIR\Downloads\07.15.2023_SRT_scrubbed.xlsx"
# xls = pd.read_excel(file_path, sheet_name="Signoff")
# try:
#     for index, row in xls.iterrows():
#         if row["TLS"] == "illia.shaban" and pd.isnull(row["Signed off"]):
#             # Update the specific cell directly in the Excel file
#             wb = openpyxl.load_workbook(file_path)
#             ws = wb["Signoff"]
#             ws.cell(row=index + 2, column=4, value="CORRECT")  # Add 2 to the row index because Excel rows start at 1
#             # Save the changes back to the same Excel file without overwriting
#             wb.save(file_path)
#             break
# except PermissionError:
#     print("Someone is using this file")
    
    
    