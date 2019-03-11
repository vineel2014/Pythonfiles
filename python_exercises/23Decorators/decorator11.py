import time

def time_dec(func):

  def wrapper(*arg):
      t = time.clock()
      res = func(*arg)
      print (func.__name__, time.clock()-t)
      return res

  return wrapper



@time_dec
def display():

    print("Display function ran")


@time_dec
def display_info(name,age,gender):

    print("Display function ran with arguments ({},{},{})".format(name,age,gender))

display_info("vineel",33,'Male')

display()







