
import subprocess

mount = subprocess.getoutput('mount -v')
lines = mount.split('\n')
points = map(lambda line: line.split()[2], lines)
 

for i in points:

    print(i)
