import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   for i in range(1,5):
      print "%s"%threadName,i 
# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   #thread.start_new_thread( print, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass
