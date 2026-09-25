def analys_number():
    # Ask the user for a number input, if it's not a whole number then it's gives an error message
    while True:
        start_value = input("Startverdi er: ")
        if start_value.isdigit():
            start_value = int(start_value)
            if start_value >= 0:
                break
        print("Bokstaver, symboler og tall som ikke er heltall er ugyldig, prøv på nytt")

    # Ask the user for a number input, if it's not a whole number then it's gives an error message
    while True:
        end_value = input("Sluttverdi er: ")
        if end_value.isdigit():
            end_value = int(end_value)
            if end_value > start_value:
                break
        print("Bokstaver, symboler, tall som ikke er heltall og hvis sluttverdien er mindre enn startverdien så er det ugyldig, prøv på nytt")


    # stars are for styling
    print("*" * 20)

    # This prints out the even number from the range
    print("Alle partall i intervallet: ", end= " ")
    for number in range(start_value, end_value + 1):
        if number % 2 == 0:
            print(number, end= " ",)

    # This print is for breaking the line
    print()

    # This prints out the number that can be divided by 3
    print("Alle tall som er delelige med 3: ", end= " ")
    for number in range (start_value, end_value + 1):
        if number % 3 == 0:
            print(number, end= " ")

    # This print is for breaking the line
    print()

    total_sum = 0
    for number in range (start_value, end_value + 1):
       total_sum += number
    print("Summen av alle tallene i intervallet", total_sum)

    print("*"*20)

analys_number()