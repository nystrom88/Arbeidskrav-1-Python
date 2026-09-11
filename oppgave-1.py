def menu ():
    print("1. Beregn tid")
    print("2. Analyser tekst")
    print("3. Analyser tallintervall")
    print("4. Avslutt ")
def total_session():
    # Keeps asking until the user enters only a whole number
    while True:
        study_session = input("Antall økter: ")
        if study_session.isdigit():
            study_session = int(study_session)
            if study_session > 0:
                break
        print("Prøv på nytt med bare postitive heltall")

    # Keeps asking until the user enters only a whole number
    while True:
        study_time = input("Tid per økt i minutter: ")
        if study_time.isdigit():
            study_time = int(study_time)
            if study_time > 0:
                break
        print("Prøv på nytt med bare postitive heltall")

    # Math to convert the total time in to minutes and hours
    total_time = study_session * study_time
    minute = total_time % 60
    hours = total_time // 60

    # The stars are for a bit of styling
    print("*" * 20)

    # Prints out the information that has been giving by the user
    print("Totalt økter:", study_session)
    print("Tid brukt per økt", study_time, "minutter")
    print(f"Totalt tid brukt er {hours} timer og {minute} minutter")

    print("*" * 20)
def analysis_text():
    # If the user input nothing or only whitespace then ask to retype agin with words
    while True:
        text_input = input("Skriv en text:")
        if text_input == "":
            print("Tom tekst er ugyldig, skriv på nytt med ord")
        elif text_input.isspace():
            print("Bare mellom rom i teksten er ugyglid, skriv på nytt med ord")
        else:
            break

    # count all items counts non-whitespace items, and reverses the input
    word_count = len(text_input)
    non_whitespace_count = len(text_input.replace(" ", ""))
    reverse_text = text_input[::-1]

    # The star are for styling
    print("*" * 20)

    # Find the word Python in the text
    find_python = "Python"
    if find_python.lower() in text_input.lower():
        print(f"Fant orde {find_python} i teksten")
    else:
        print("Innholder ikke orde Python i teksten")

    # Print out the text that the user typed in
    print(f"Antall tegn med mellomrom {word_count} og uten mellomrom {non_whitespace_count}", )
    print(f"Teksten i små bokstaver: {text_input.lower()}")
    print(f"Teksten baklegs: {reverse_text}")
    print("*" * 20)
def analysis_number():
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
        print(
            "Bokstaver, symboler, tall som ikke er heltall og hvis sluttverdien er mindre enn startverdien så er det ugyldig, prøv på nytt")

    # stars are for styling
    print("*" * 20)

    # This prints out the even number from the range
    print("Alle partall i intervallet: ", end=" ")
    for number in range(start_value, end_value + 1):
        if number % 2 == 0:
            print(number, end=" ", )

    # This print is for breaking the line
    print()

    # This prints out the number that can be divided by 3
    print("Alle tall som er delelige med 3: ", end=" ")
    for number in range(start_value, end_value + 1):
        if number % 3 == 0:
            print(number, end=" ")

    # This print is for breaking the line
    print()

    total_sum = 0
    for number in range(start_value, end_value + 1):
        total_sum += number
    print("Summen av alle tallene i intervallet", total_sum)
    print("*" * 20)
def main():
    while True:
        menu()
        user_choice = input("Hva vil du velge: ")
        if user_choice == "1":
            total_session()

        elif user_choice == "2":
            print("Analyser text")
            analysis_text()

        elif user_choice == "3":
            print("Analyser number")
            analysis_number()

        elif user_choice == "4":
            print("Avslutt program")
            break
        else:
            print("Går ikke, velg mellom 1-4")

if __name__ == "__main__":
    main()

