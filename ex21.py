def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Basic Mathematical Calculations through some functions with return values"

num1 = int(raw_input("Enter num1 : "))
num2 = int(raw_input("Enter num2 : "))

p = add(num1, num2)
q = subtract(num1, num2)
r = multiply(num1, num2)
s = divide(num1, num2)

print "p: %d, q: %d, r: %d, s: %d" % (p, q, r, s)


# Now Let's do something really cool......
print "Combining all the Functions....Passing the return value of one function as argument to other"

cool = add(p, subtract(q, multiply(r, divide(s, 2))))

print "That becomes: ", cool, ". Now, that's cool. Isn't it?"
