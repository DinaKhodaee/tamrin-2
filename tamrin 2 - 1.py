import math
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
p = x+y
print("Sum =", p)
if x>y:
    s = x-y
    print("Subtraction =", s)
else:
    ss = y-x
    print("Subtraction =", ss)
mul = x*y
print("Multiplication =", mul)
if x>y:
    div = x/y
    print("Division =", div)
else:
    div1 = y/x
    print("Division =", div1)
radical1 = math.sqrt(x)
print("Radical x =", radical1)
radical2 = math.sqrt(y)
print("Radical y =", radical2)
tan1 = math.tan(x)
print("Tanzhant x =", tan1)
tan2 = math.tan(y)
print("Tanzhant y =", tan2)
sin1 = math.sin(x)
print("Sinous x =", sin1)
sin2 = math.sin(y)
print("Sinous y =",sin2)
cos1 = math.cos(x)
print("Cosinous x =", cos1)
cos2 = math.cos(y)
print("Cosinous y =", cos2)
