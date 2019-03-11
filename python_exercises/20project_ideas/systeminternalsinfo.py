import psutil
import datetime
#information about CPU

#s=psutil.sensors_temperatures()

s1=psutil.cpu_count()

#print("CPU TEMEPATURE:",s)

#print("CPU FANS:",psutil.sensors_fans())

print("CPU COUNT:",s1)

print("CPU COUNT (PHYSICAL)", psutil.cpu_count(logical=False))

#print( "CPU FREQUENCY:",psutil.cpu_freq())

#print("CPU FREQUENCY(PER CORE):",psutil.cpu_freq(percpu=True))

print("CPU UTILIZATION(PER CORE):",psutil.cpu_percent(interval=1, percpu=True))

print("CPU STATISTICS:",psutil.cpu_stats())

print("CPU'S VIRTUAL MEMORY:",psutil.virtual_memory())

print("CPU'S SWAP MEMORY:",psutil.swap_memory())


#Information about disk

print("DiSK PARTITIONS:",psutil.disk_partitions())

print("DISK USAGE:",psutil.disk_usage('/'))

print("DISK I/O DETAILS:",psutil.disk_io_counters())

#Information about network

print("NETWORK I/O DEATILS:",psutil.net_io_counters())

print("NETWORK CONNECTON TYPES:",psutil.net_connections())

print("NETWORK IP ADDRESS:",psutil.net_if_addrs())

print("NETWORK INTERFACE CARD INFORMATION:",psutil.net_if_stats())


#Laptop battery details

#print("BATTERY DETAILS:",psutil.sensors_battery())

#System boot time

print("SYSTEM BOOT ON TIME:",datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

#System users

print("SYSTEM USERS:",psutil.users())

#System running Process IDs

print("System Running Process ID'S:",psutil.pids())


