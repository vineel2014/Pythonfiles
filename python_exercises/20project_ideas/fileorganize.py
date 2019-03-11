#************INTERNET SPEED TEST PROGRAM*********************
# __AUTHOR__: VINEEL KUMAR
# VERSION:1.0
#************************************************************
import os
import subprocess
import shutil

# --------------------------------------------------------
reorg_dir = "/home/vineel/Downloads"
exclude = () # for example
remove_emptyfolders = True
# ---------------------------------------------------------

def dir_names(ext):
    extensions = [
        [["jpeg", "jpg", "png"], "Pictures"],
        [["mp4", "avi","mkv","mpg","mpeg","ogg"], "Videos"],
        [["docx", "doc", "pdf", "xlsx", "ppt", "pptx"], "Documents"],
        [["mp3"], "Music"],
        [["db"], "Database"],
        [["zip","gz","bz","rar"], "Archives"],
        [["deb"], "Debian"],
        [["iso"], "ISOimages"],
        [["exe"], "Executables"],
        [["log"], "logfiles"],
        [["py"], "Python"],
        [["java"], "JAVA"],
      
        ]
    match = [item[1] for item in extensions if ext.lower() in item[0]]
    return match[0] if match else "Others"

for root, dirs, files in os.walk(reorg_dir):
    for name in files:
        subject = root+"/"+name
        if name.startswith("."):
            extension = "hidden_files"
        elif not "." in name:
            extension = "without_extension"
        else:
            extension = dir_names(name[name.rfind(".")+1:]) # edited line
        if not extension in exclude:
            new_dir = reorg_dir+"/"+extension
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            shutil.move(subject, new_dir+"/"+name)

def cleanup():
    filelist = []
    for root, dirs, files in os.walk(reorg_dir):
        for name in files:
            filelist.append(root+"/"+name)
    directories = [item[0] for item in os.walk(reorg_dir)]
    for dr in directories:
        matches = [item for item in filelist if dr in item]
        if len(matches) == 0:
            try:
                shutil.rmtree(dr)
            except FileNotFoundError:
                pass

if remove_emptyfolders == True:
    cleanup()
