x = input("Number 1: ")
y = input("Number 2: ")

op = raw_input("Enter operation + | - | * | /: ")

if op == '+':
    print x+y
elif op == '-':
    print x-y
elif op == '*':
    print x*y
elif op == '/':
    print float(x)/y
else:
    print "Invalid operator"
