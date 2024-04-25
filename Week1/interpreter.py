a = input("Expression:").strip().split(" ")
x = int(a[0])
z = int(a[2])
y = a[1]
if y == '+':
    print("{:.1f}".format(x+z))
elif y == '-':
    print("{:.1f}".format(x-z))
elif y == '*':
    print("{:.1f}".format(x*z))
elif y == '/':
    if z == 0:
        print("error")
    else:
        print("{:.1f}".format(x/z))
else:
    print("error")
# other elegent  way       
#x, y, z = input("Expression: ").split()

#x, z = int(x), int(z)
#ans = eval(f"{x} {y} {z}")

#print(f"{ans:.1f}")