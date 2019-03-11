import os
import zipfile
import datetime

start=datetime.datetime.now()

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
    
        if '.git' in dirs:

            dirs.remove('.git')

        if '.idea' in dirs:

            dirs.remove('.idea')

        for file in files:
    
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('/home/vineel/pythonexercises.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('.', zipf)
    zipf.close()

end=datetime.datetime.now()

print("Time taken for zipping:",end-start)
