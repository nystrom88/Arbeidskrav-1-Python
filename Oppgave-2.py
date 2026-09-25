# Here is where the register data is appended to
def dummy_data(topic, durtaion_minutes, status ):
    data = {"Økter": topic,
            "Minutter": durtaion_minutes,
            "Status": status}
    return data

# Here is where the functions are executed
def main():
    #where the data from register is stored
    study_session_database = []

    # Here are the five data examples
    study_session_database.append(dummy_data("Norsk",45, "Planlagt"))
    study_session_database.append(dummy_data("Engelsk", 90, "Planlagt"))
    study_session_database.append(dummy_data("Tysk", 45, "Ferdig"))
    study_session_database.append(dummy_data("Svensk", 32, "Planlagt"))
    study_session_database.append(dummy_data("Matte", 120, "Ferdig"))

    # When user types in an input then execute that function
    menu()
    while True:
        velg_meny = input("Hva vil du velge: ")
        if velg_meny.isdigit():
            velg_meny = int(velg_meny)
            if velg_meny == 1:
                study_session_database.append(register())
            elif velg_meny == 2:
                 show_session(study_session_database)
            elif velg_meny == 3:
                show_done_session(study_session_database)
            elif velg_meny == 4:
                theme_session(study_session_database)
            elif velg_meny == 5:
                sorted_session(study_session_database)
            elif velg_meny == 6:
                total_session(study_session_database)
            elif velg_meny == 7:
                print("Avslutt program")
                break

        # if input is not correct the give error message
            else:
                print("kun velg mellom 1-7")
        else:
            print("kun velg mellom 1-7")
        menu()

# Display the option the user can choose
def menu():
    print("1. Registrere en studieøkt")
    print("2. Vise alle studieøkter")
    print("3. Vise bare fullførte studieøkter")
    print("4. Søke etter et ord i temaet")
    print("5. Sortere øktene etter varighet, lengst først")
    print("6. Vise samlet og gjennomsnittlig varighet for fullførte økter")
    print("7. Avslutte programmet")

#function for register the sessions
def register():
    # user input on what the session is called
    while True:
        topic = input("Skriv in en økt: ")
        if topic.isdigit():
            print("kan ikke bare inneholde tall")
        elif topic == "":
            print("Tom tekst er ugyldig, skriv på nytt med ord")
        elif topic.isspace():
            print("Bare mellom rom i teksten er ugyglid, skriv på nytt med ord")
        else:
            break

    # user input on how long the session is
    while True:
        duration_minutes = input("Tid på økten i minutter: ")
        if duration_minutes.isdigit():
            duration_minutes = int(duration_minutes)
            if duration_minutes > 0:
                break
        print("Prøv på nytt med bare postitive heltall")

    # user can choose between planned or completed
    while True:
        status = input("Skriv 1. for Planlagt eller 2. for Ferdig: ")
        if status.isdigit():
            status = int(status)
            if status == 1:
                status = "Planlagt"
                break
            elif status == 2:
                status = "Ferdig"
                break
        # gives error message if the user dos not type 1 or 2
            else:
                print("Kan kun velge mellom 1 eller 2")
        else:
            print("Kan kun velge mellom 1 eller 2")

    # the stars styling
    print("*"*25)

    print(f"Studie Økt: {topic} brukt  {duration_minutes} minutter og økten er {status}")
    min_data = {"Økter": topic,
                "Minutter": duration_minutes,
                "Status": status}

    print("*" * 25)
    return min_data


#function for displaying all the register sessions
def show_session(study_session_database):

    print("*" * 25)
    #prints out all the sessions
    for x in study_session_database:
        print(f"Økt: {x["Økter"]}, {x["Minutter"]} Minutter, status: {x["Status"]}")
    print("*" * 25)

#function for only displaying if the sessions is completed
def show_done_session (study_session_database):
    print("*" * 25)
    for x in study_session_database:
        if x["Status"] == "Ferdig":
            # prints out only the completed sessions
            print(f"Økt: {x["Økter"]}, {x["Minutter"]} Minutter, status: {x["Status"]}")
    print("*" * 25)

#function for when the user can search for a registered session
def theme_session(study_session_database):
    while True:
        # display the registered sessions that can be searched on
        print("valgene du har er:", end= " ")
        for x in study_session_database:
            print(f"{x["Økter"]}", end=", ")
        print()

        theme = input(f"Søk etter en av disse fagene: ")
        test = False

        print("*" * 25)
        # display only what has been search on
        for x in study_session_database:
            if x["Økter"] == theme:
                print(f"Økt: {x["Økter"]}, {x["Minutter"]} Minutter, status: {x["Status"]}")
                print("*" * 25)
                test = True

        #if user don't know any session the give examples so not to be stuck in the loop
        if test == False:
            print("Prøv på nytt")
        if test == True:
            break
        print("*" * 25)


#function for sorting the sessions by high to low
def sorted_session(study_session_database):
    new_list = sorted(study_session_database, key=lambda økt_tid:økt_tid["Minutter"], reverse=True)
    print("*" * 25)
    for x in new_list:
        # display the list from high to low on minutes
        print(f"Økt: {x["Økter"]}, {x["Minutter"]} Minutter, status: {x["Status"]}")
    print("*" * 25)

#function for showing total time and average time for completed sessions
def total_session(study_session_database):
    total_tid = 0
    counter = 0
    for x in study_session_database:
        if x["Status"] == "Ferdig":

            total_tid = total_tid + x["Minutter"]
            counter = counter +1

    gjenomsnitt = total_tid // counter
    print("*" * 25)
    # display total minutes and average minutes
    print(f"Total tiden: {total_tid} minutter")
    print(f"gjenmsnitt tiden er {gjenomsnitt} minutter")

    print("*" * 25)




if __name__ == "__main__":
    main()



