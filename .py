question = "Guess a number"
n = 0
while True:
    print("Type q to quit")
    answer = input(question)
    if answer == "q":
        break
    elif answer == "9":
        print("That's right!")
    else:
        print("Wrong!")
