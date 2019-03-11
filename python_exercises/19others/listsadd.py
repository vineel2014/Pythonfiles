def add_lists(a_list,b_list):
    sum_list=[]
    for index in range(len(a_list)):
        sum=a_list[index]+b_list[index]
        sum_list.append(sum)
    return sum_list
a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=add_lists(a,b)
print(c)

