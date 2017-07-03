from openpyxl import load_workbook

wb = load_workbook("Online Document Database.xlsx")
sheet_names=wb.get_sheet_names() # list of sheet names # list of strings

file_object =open("ref_list.txt","w")
i_am_gay = True
for i in range(0,len(sheet_names)):
    sheet=wb[sheet_names[i]]
    file_object.write(sheet_names[i])
    file_object.write("\n")
    for row in sheet.rows:
        i_am_gay = True
        for cell in row:
            if i_am_gay==True:
                h = cell.value
                i_am_gay=False
            else:
                G = cell.value
                if G == None:
                    j0=0

                else:
                    file_object.write(str(G))
                    file_object.write(" ")
        file_object.write("\n" + "\n" )
    file_object.write("\n" + "\n" + "\n")
