import math
sum = 0
number = int(input("Enter the number of students: "))
for i in range (number):
    mark = float(input("Enter the mark: "))
    sum += mark
    avg = sum/number
print("Class avg is = ", avg)
#print("minimum in class =")
#print("Maximum in class =")