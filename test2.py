while True:
    print("=== Calculator ===")
    print("Choose from option 1(addition), 2(substraction), 3(multiplication), 4(division) or 5(leave)")
    guess = int(input("Enter option 1, 2, 3, 4, 5: "))

    if guess == 1:
        print("Perfect! You chose addition!")
        add1 = float(input("Enter the first number: "))
        add2 = float(input("Enter the second number: "))
        resultadd = add1 + add2
        print(resultadd)

    elif guess == 2:
            print("Amazing! You chose substraction!")
            sub1 = float(input("Enter the first number: "))
            sub2 = float(input("Enter the second number: "))
            resultsub = sub1 + sub2
            print(resultsub)

    elif guess == 3:
            print("Great! You chose multiplication!")
            mul1 = float(input("Enter the first number: "))
            mul2 = float(input("Enter the second number: "))
            resultmul = mul1 + mul2
            print(resultmul)

    elif guess == 4:
                print("Bravo! You chose division!")
                divi1 = float(input("Enter the first number: "))
                divi2 = float(input("Enter the second number: "))
                resultdivi = divi1 + divi2
                print(resultdivi)

    else:
           print("Bye! Hope to see you soon!")
           break

