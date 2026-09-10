def analys_text():
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
    non_whitespace_count = len(text_input.replace(" ",""))
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
    print(f"Antall tegn med mellomrom {word_count} og uten mellomrom {non_whitespace_count}",)
    print(f"Teksten i små bokstaver: {text_input.lower()}")
    print(f"Teksten baklegs: {reverse_text}")

    print("*"*20)
analys_text()