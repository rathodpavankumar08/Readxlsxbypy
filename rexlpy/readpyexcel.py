import xlrd
wb=xlrd.open_workbook("Readpyexc.xlsx")
sheet=wb.sheet_by_index(0)
for val in range(sheet.nrows):
    print(sheet.cell_value(val,0),sheet.cell_value(val,1),sheet.cell_value(val,2))

print("number of cols ",sheet.ncols)
print("number of rows",sheet.nrows)
