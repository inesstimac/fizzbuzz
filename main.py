while True:
    number = int(input("Enter a number between 1 and 100: "))

    for value in range(1, number + 1):
        if value % 3 == 0:
            print("fizz")
        elif value % 5 == 0:
            print("buzz")
        elif value % 3 == 0 and value % 5 == 0:
            print("fizzbuzz")
        else:
            print(value)

    question = input("Do you want to play again? ")
    if question == "no":
        break
