# This exercise explains the use of functions

# this one is like the scripts with argv
def print_three(*args):
    arg1, arg2, arg3 = args
    print "arg1: %r, arg2: %r, agr3: %r" % (arg1, arg2, arg3)

# ok, that *args is actually pointless, we can just do this
def print_three_again(arg1, arg2, arg3):
    print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_three("Dheeraj","Kumar","Ketireddy")
print_three_again("Dheeraj","Kumar","Ketireddy")
print_one("First!")
print_none()
