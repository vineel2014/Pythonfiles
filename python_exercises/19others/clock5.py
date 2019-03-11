import time
def procedure():
    time.sleep(2.5)

t0=time.clock()
print(t0)

procedure()
print(time.clock()-t0,'Seconds process time')

t0=time.time()
procedure()

print(time.time()-t0,'seconds wall time')
