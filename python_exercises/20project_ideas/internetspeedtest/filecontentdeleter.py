#created to run for cronjob
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()
    pfile.close()

pfile=open("speedtest.log","rb+")
deleteContent(pfile)
