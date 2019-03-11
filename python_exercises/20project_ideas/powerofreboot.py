import os
import platform

user=platform.node()
print("SYSTEM:",user)


#works in Linux

print()
print("CHOICES:")
print("1:REBOOT")
print("2:POWEROFF")
print("3:LOGOUT")
print("4:SUSPEND")

try:

    s=int(input("Enter your choice:"))

    if s==1:

        os.system("systemctl reboot -i")

    elif s==2:

        os.system("systemctl poweroff -i")
    
    elif s==3:
             
        os.system( "sudo pkill -u" + user )

    elif s==4:

        os.system("systemctl suspend -i")

    else:

        print("you entered wrong choice")

except:

    print("Wrong input given")
