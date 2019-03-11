import datetime
import os

start=datetime.datetime.now()

os.system("sudo git status")
os.system("sudo git add --all")
os.system("git status")
os.system("sudo git commit -m 'First commit'")

os.system("sudo git push")
os.system("git status")

end=datetime.datetime.now()

print("Time taken to push into GITHUB:",end-start)





