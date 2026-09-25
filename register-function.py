def register():
    while True:
        topic = input("Skriv in en økt: ")
        if topic.isdigit():
            print("kun ord uten tall")
        elif topic == "":
            print("Tom tekst er ugyldig, skriv på nytt med ord")
        elif topic.isspace():
            print("Bare mellom rom i teksten er ugyglid, skriv på nytt med ord")
        else:
            break

    while True:
        duration_minutes = input("Tid på økten i minutter: ")
        if duration_minutes.isdigit():
            duration_minutes = int(duration_minutes)
            if duration_minutes > 0:
                break
        print("Prøv på nytt med bare postitive heltall")

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
            else:
                print("Kan kun velge mellom 1 eller 2")

    print(f"Studie Økt: {topic} brukt  {duration_minutes} minutter og økten er {status}")
    min_data ={"økter": topic,
               "minutter": duration_minutes,
               "status": status}
    return min_data
register()