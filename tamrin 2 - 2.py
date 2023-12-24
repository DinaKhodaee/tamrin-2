h = float(input("Enter your height (m): "))
w = int(input("Enter your weight (kg): "))
bmi = w/h*h
print("Your bmi is =", bmi)
if bmi <= 18.5:
    print("Underweight.")
elif bmi >= 18.5 or bmi <= 24.9:
    print("Normal Weight.")
elif bmi >= 25 or bmi <= 29.9:
    print("Overweight.")
elif bmi >= 30:
    print("Obesity.")