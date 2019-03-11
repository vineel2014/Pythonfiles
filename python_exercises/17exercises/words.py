import win32com.client as win32

wrd = win32.Dispatch("word.Application")
ss = wrd.Documents.Add()
wrd.Visible = True

rng = ss.Range(0,0)
rng.InsertAfter('something')

ss.SaveAs(r'C:\Users\Dell\Desktop\Lovely Codes\word.doc')

ss.Close()
wrd.Application.Quit()
