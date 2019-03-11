def minmax_list(a_list):
    min_so_far = a_list[0]
    max_so_far = a_list[0]
    for a in a_list :
        if a < min_so_far:
            min_so_far = a
        if a > max_so_far:
            max_so_far = a
    return min_so_far, max_so_far
c=[1,2,3,4]
e=minmax_list(c)
print(e)

