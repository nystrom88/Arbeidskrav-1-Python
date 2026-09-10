def total_session():
    # Keeps asking until the user enters only a whole number
    while True:
        study_session = input("Antall økter: ")
        if study_session.isdigit():
            study_session = int(study_session)
            if study_session > 0 :
                break
        print("prøv på nytt med bare postitive heltall")

    # Keeps asking until the user enters only a whole number
    while True:
        study_time = input("Tid per økt i minutter: ")
        if study_time.isdigit():
            study_time = int(study_time)
            if study_time > 0:
                break
        print("prøv på nytt med bare postitive heltall")

    # Math to convert the total time in to minutes and hours
    total_time = study_session * study_time
    minute = total_time % 60
    hours = total_time // 60

    # The stars are for a bit of styling
    print("*"*20)

    # Prints out the information that has been giving by the user
    print("Totalt økter:", study_session)
    print("Tid brukt per økt", study_time, "minutter")
    print(f"Totalt tid brukt er {hours} timer og {minute} minutter")

    print("*"*20)

total_session()


