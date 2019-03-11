from github3 import login
import github3
import os

gh = github3.login(username='vineel2006@gmail.com', password='#$123vin$#')
repository = gh.repository('vineel2014', 'pythonfiles')

files_to_upload=[]
for file in os.listdir(os.curdir):
    files_to_upload=file
    print (file)

for file_info in files_to_upload:
    try:
        with open(file_info, 'rb') as fd:
            contents = fd.read()
        repository.create_file(
            path=file_info,
            message='Start tracking {!r}'.format(file_info),
            content=contents,
           )
    except:
        print("Code Pushed")
