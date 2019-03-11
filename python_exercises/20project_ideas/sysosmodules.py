import sys
#import os,pwd
#Standard Library - https://docs.python.org/3/library/index.html

#Thia Python program covers os and sys modules

def main():
    
    import os,pwd  

    print("***********OS MODULE*************")

    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.listdir())
    if os.path.isdir('/home/vineel/practpy/python_exercises/20project_ideas/vvk'):
        os.rmdir('vvk')
            
    os.mkdir('vvk')
    print(os.listdir())
    print(os.rename('vvk','vineel'))
    print(os.listdir())
    print(os.rmdir('vineel'))
    print(os.listdir())
    l=os.walk(os.getcwd())
    for i in l:
        print (i)
    print(os.path.basename('vineel'))
    if os.path.isdir('/home/vineel/practpy/python_exercises/20project_ideas/vvk'):
        os.rmdir('vvk')
    
    os.mkdir('vvk')
    print(os.listdir())
    k=os.path.isdir('/home/vineel/practpy/python_exercises/20project_ideas/vvk')
    print(k)


    os.system('python3 welcome.py')
    print(os.getuid())
    print(os.getpid())
    print(os.getgid())
    print(os.stat('/home/vineel/practpy/python_exercises/20project_ideas/welcome.py'))
    print(os.path.getsize('/home/vineel/practpy/python_exercises/20project_ideas/welcome.py'))
    print(pwd.getpwuid(os.getuid())[0])
    print(os.getgroups())
    print(os.ctermid())
    print(os.getpgrp())
    print(os.system('who'))
    print(os.system('ls -l'))
    print("hai")
    print(os.system("ls *.py"))
    if os.path.isdir('/home/vineel/practpy/python_exercises/20project_ideas/hai'):
        os.rmdir('hai')
    print(os.makedirs("/home/vineel/practpy/python_exercises/20project_ideas/hai"))
    print(os.listdir())
    print(os.removedirs("/home/vineel/practpy/python_exercises/20project_ideas/hai"))
    print(os.listdir())
    print("***************SYS MODULE****************")
    #print("SYSTEM VERSION INFORMATION:",sys.version_info)
    #print("SYSTEM PLATFORM:",sys.platform)
    sys.stderr.write('This is stderr text\n')
    sys.stderr.flush()
    sys.stdout.write('This is stdout text\n')
    print ("This is the name of the script: ", sys.argv[0])
    print ("Number of arguments: ", len(sys.argv))
    print ("The arguments are: " , str(sys.argv))
    print ('\n'.join(sys.modules.keys()))
    """    # it's easy to print this list of course:
    print (sys.argv)

    # or it can be iterated via a for loop:

    for i in range(len(sys.argv)):
        if i == 0:
            print ("Function name: %s" % sys.argv[0])
        else:
            print ("%d. argument: %s" % (i,sys.argv[i])"""

    # it's easy to print this list of course:
    print (sys.argv)

    # or it can be iterated via a for loop:

    for i in range(len(sys.argv)):
        if i == 0:
            print ("Function name: %s" % sys.argv[0])
        else:
            print ("%d. argument: %s" % (i,sys.argv[i]))

    for i in (sys.stdin, sys.stdout, sys.stderr):
        print(i)

    print(sys.byteorder)
    print(sys.executable)
    print(sys.maxsize)
    print(sys.maxunicode)
    print(sys.path)
    print(sys.platform)
    print(sys.version)
    print(sys.version_info)
    print(sys.getrecursionlimit())
    print(sys.setrecursionlimit(5000))
    print(sys.getrecursionlimit())
   
    def dump(module):
        print (module, "=>",)
        
        if module in sys.builtin_module_names:
            print ("<BUILTIN>")
        else:
            module = __import__(module)
                
            print ("NOT A BUITLIN MODULE:",module.__file__)

    dump("os")
    dump("sys")
    dump("string")
    #dump("strop")
    dump("zlib")
    
    variable = 1234

    print (sys.getrefcount(0))
    print (sys.getrefcount(variable))
    print (sys.getrefcount(None))
    
    

#
# emulate "import os.path" (sort of)...

    if sys.platform == "win32":
        import ntpath
        pathmodule = ntpath
    elif sys.platform == "mac":
        import macpath
        pathmodule = macpath
    else:
    # assume it's a posix platform
        import posixpath
        pathmodule = posixpath

    print (pathmodule)
    
    print(dir(sys))
    print(sys.warnoptions)
    """print("EXII FROM PROGRAM USING SYS.EXIT():")
    sys.exit(1)"""

    print(sys.exc_info)
    print(sys.exec_prefix)
    print(sys.flags)
    print(sys.float_info)
    print()
    print(sys.abiflags)
    print(sys.base_exec_prefix)
    print()
    print(sys.modules,end=" ")
    print()
    print(sys.meta_path)
    print(sys.int_info)

if __name__ == "__main__": main()
