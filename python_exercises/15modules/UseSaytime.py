import time, saytime

t = time.localtime()

print(
    "In Bangalore, India, it is now " +
    saytime.saytime_t(t).words() +
    time.strftime(', on %a, %d %b %Y.')
)

