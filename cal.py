a = int(input("enter a number:"))
b = int(input("enter a number(no 0):"))

op = input("enter any operation in (+,-,x,/)")

sum = a+b
diff = a-b
mux = a*b
div = a/b

if op == '+':
    print("sum", sum)
elif op == '-':
    print("difference", diff)
elif op == 'x':
    print("multipy", mux)
else:
    print("division", div)


