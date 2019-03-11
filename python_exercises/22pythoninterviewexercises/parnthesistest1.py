def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

str=input("Enter a string with paranthesis:")
print("Open and close paranthesis matches:",matched(str))

