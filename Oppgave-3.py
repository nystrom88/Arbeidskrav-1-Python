from datetime import datetime, timedelta

def main():
    menu()
    while True:
        choose = input("Velg en funksjon: ")
        if choose.isdigit():
            choose = int(choose)

            if choose == 1:
                while True:
                    date_input = input("Skriv in en med format dd.mm.åååå: ")

                    date_display = date_function(date_input)
                    if not date_display == False:
                        print(date_display)
                    break

                # tar imot en dato på formatet dd.mm.åååå og returnerer en datoverd
            elif choose == 2:
                while True:
                    try:
                        date_input = input("Skriv in starts tid i format tt:mm ")
                        minute_input = int(input("Hvor lenge varer økten i minutter: "))
                        display_end_time = display_time(date_input, minute_input)
                        print(display_end_time)
                        break

                    except TypeError:
                        print("formate du skrev er feil")
                    except ValueError:
                        print("hvor lenge økten varer kan kun skrives med posetiv hel tall")

                # tar imot starttidspunkt og minutter og returnerer sluttid


            elif choose == 3:
                while True:
                    try:
                        start_day = input("formate er dd.mm.åååå skriv in start dato: ")
                        end_day = input("Formate er dd.mm.åååå skriv in sluttdato: ")
                        display_sluttid = count_days(start_day, end_day)
                        print(display_sluttid)
                        break
                    except ValueError:
                        print("Prøv på nytt, formate er dd.mm.åååå")



                # tar imot to datoer og returnerer positivt antall dager mellom dem
            elif choose == 4:
                dummy_list = [datetime.strptime("08.08.2002", "%d.%m.%Y"),
                              datetime.strptime("23.04.2025", "%d.%m.%Y"),
                              datetime.strptime("12.07.2012", "%d.%m.%Y"),
                              datetime.strptime("29.06.1996", "%d.%m.%Y"),
                              datetime.strptime("09.12.1990", "%d.%m.%Y")]
                break_loop = False
                while True:
                    try:
                        dummy_input = datetime.strptime(input("Skriv en dato i format dd.mm.åååå: "), "%d.%m.%Y")
                        dummy_list.append(dummy_input)
                    except ValueError:
                        print("Datoen du skrev er feil prøv på nytt, bokstaver og tegn som ikker er '.' er ugyldig" )
                        print("eksmpel på en gydlig dato er '20.04.2025'")


                    while True:
                        yes_or_no = input("Vil du legge til en til dato y/n: ").lower()

                        if yes_or_no== "y":
                            break
                        elif yes_or_no =="n":
                            break_loop = True
                            break
                        else:
                            print("y eller n")

                    if break_loop == True:
                        break

                date_test_list = date_sort(dummy_list)
                print(date_test_list)

                # tar imot en list med datoer og returnerer en kronologisk sortert list
            elif choose == 5:
                break
            else:
                print("Kun velg mellom 1-5")
        menu()
def menu():
    print("1. Gjør om til dato")
    print("2. Vis sluttid")
    print("3. Vis dager mellom to datoer")
    print("4. Vis en list med datoer")
    print("5. Avslutt programmet")



def date_function(dato_text):
    try:
        date_object = datetime.strptime(dato_text, "%d.%m.%Y")
        date_object_text = date_object.strftime("%d.%m.%Y")
        return date_object_text
    except (ValueError, TypeError):
        return "Prøv på nytt. Se om du har skrevet riktig"


def display_time(start_time, minute_time):
    try:
        start_date_object = datetime.strptime(start_time, "%H:%M")
        delta = timedelta(minutes=minute_time)
        total_time = start_date_object + delta
        return total_time.strftime("%H:%M")
    except (ValueError, TypeError):
        return "Prøv på nytt. Se om du har skrevet riktig"



def count_days(delta_, delta__):
    delta_one = datetime.strptime(delta_, "%d.%m.%Y")
    delta_two = datetime.strptime(delta__, "%d.%m.%Y")

    end_date = delta_two - delta_one
    return abs(end_date.days)

def date_sort(date_list):
    list_ = sorted(date_list)
    new_list = []
    for x in list_:
        new_list.append(x.strftime("%d.%m.%Y"))

    return new_list


if __name__ == "__main__":
    main()