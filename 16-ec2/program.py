x = 1
if x == 1:
    x = 2
else:
    x = 3

def add(a, b):
    return a + b

# each 100% , 70%

# find the maximum of two numbers
# if zero is provided as either argument, it returns -1
def max1(a, b):
    if a == 0 or b == 0:
        return -1

    if a >= b:
        return a
    else:
        return b

# returns 0 when max returns -1
def uses_max1():
    a = 10
    b = 0
    result = max1(a, b)
    if result == -1:
        return 0
    else:
        result


#print(add("Hello ", " World"))

