import win32com.client as win32

xl = win32.Dispatch("Excel.Application")
ss = xl.Workbooks.Add()
sh = ss.ActiveSheet
xl.Visible = True

sh.Cells(1,1).Value = 'something'
sh.SaveAs(r'C:\Users\Dell\Desktop\Lovely Codes\excel.xls')

ss.Close()
xl.Application.Quit()
