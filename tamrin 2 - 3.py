for i in range (3):
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    m1 = float(input("Enter your first mark: "))
    m2 = float(input("Enter your second mark: "))
    m3 = float(input("Enter your third mark: "))
    avg = (m1+m2+m3) / 3
    print(fname, lname, "Your average is =", avg)
    if avg >= 18:
        print("Exellent!")
    elif avg < 18 and avg >= 10:
        print("Good!")
    elif avg < 10:
        print("Failed!")