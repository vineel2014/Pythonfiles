def product(numbers):
    sum_so_far=1
    for number in numbers:
        sum_so_far*=number
    return sum_so_far

print(product([1,2,3]))
print(product([7,-4,1,6,0]))
print(product([]))


