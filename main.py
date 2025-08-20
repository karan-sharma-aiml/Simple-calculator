try:
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))

    print("what kind of operation do you want to perform.Press + for addition\n press - for subtraction\n press * for multiplication\n press / for divison")

    o = input("enter operation")
    match o:
        case "+":
            print(f"The sum of {a + b}")
        case "-":
            print(f"The substraction of two number is {a -b}")
        case "*":
            print(f"The multiplication of {a * b}")
        case "/":
            print(f"The divide of two number is {a/b}")

except Exception as e:
    print("enter the valid value of a and b")