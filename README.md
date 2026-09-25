# Arbeidskrav 1 Readme.md




# dumkumentajon

## Oppgave 2
#### Data struktur
data strukturen bruker er dictionary og list.  
Fordi med dictionary så kan ha spesefike keys som finner og lagrer informajon

``` 
    data = {"Økter": topic,
            "Minutter": durtaion_minutes,
            "Status": status}
``` 
her så ser vi at Økter, Minutter og status som Key og topic, durtaion_minutes,
status som value fordi når brukren inputer hva økten heter. Så vil Økten lagres i valuen "topic" og når vi kaller fram keyen "Økter"
som er knytet til "topic" så vil den finne fram økt navne som brukren skrev in.  

med at vi lagrer en setning med de valuene så er dictionary være greit å bruke fordi med dictionary
så kan den ikke ha den samme keyen flere ganger i samme dictionary.

Jeg bruker også "list" i datastrukturen min fordi jeg skal lagre flere registreringer, hver registrering i listen er en dictionary. 
Med list synes jeg at det blir lettere å finne fram dataen når jeg bruker en for loop.

eksmple under her viser hvordan flere dicts er lagret i en liste
```
dummy_data =
[{'Minutter': 45, 'Status': 'Planlagt', 'Økter': 'Norsk'}, 
{'Minutter': 90, 'Status': 'Planlagt', 'Økter': 'Engelsk'}, 
{'Minutter': 45, 'Status': 'Ferdig', 'Økter': 'Tysk'}, 
{'Minutter': 32, 'Status': 'Planlagt', 'Økter': 'Svensk'}, 
{'Minutter': 120, 'Status': 'Ferdig', 'Økter': 'Matte'}]
```

programmet er bygget opp i flere functioner og fucntionene blir kjørt i main.  
jeg har 9 funksjoner i programmet  
def dummy_data(): er der rgeistreringene blir lagret med keys.  
def main(): er der alle funksjonene mines skal kjøre.  
def menu(): her så vil man se hva brukren kan velge mellom.  
def register(): er så vil brukren bli spørt om å registere øktene sine
def show_session(): her vises alle registeringne som var i coden fra før av og hva brukren legger in.  
def show_done_session(): alle registeringene som har staus som ferdig blir vist her.  
def theme_session(): her får kan man søke etter et tema og få opp alle registeringene med samme navn.  
def sorted_session(): sorterer alle øktene fra lengst minutter til minst minutter.  
def total_session(): vsier total tid og gjennomsnits tiden til sammen av alle øktene som har status "ferdig".  




## Oppgave 3
I programmet mitt bruker jeg import datetime. 
men jeg har satt det opp som "from datetime import datetime, timedelta"  
det gjør er at jeg heter det jeg synes nødvendig fra modulen sånn at koden kan se bedre ut og mer forståelig.  

hvis hadde bare import datetime vil det se sånn ut
```
total_time = datetime.datetime.now() - datetime.timedelta(minutes = 30)
```

når jeg bruker from datetime import datetime, timedelta så vil det se sånn ut
````
total_time = datetime.now() - timedelta(minutes = 30)
````



gyldig og ugylidg testtilfeller  
    
| funkjoner| testtilfeller gyldig|testtilfeller ugylidg |
| :---     | :---:    | ---:     |
| date_function    |"20.05.2025"  |"08:08:2002"|
| date_function    |"2.8.2027"    | "Hei"    |
|display_time      |"14:30", 120  |"12.45", "trf"   |
|display_time      | "8:2", 45    |"26:45", 56   |
|count_days        |"01.11.2026", "25.11.2026"|"test", "20.02.2025" |
|count_days        |"23.06.2026", "12.03.2025"| "23:04.2026", "23.18.2026"|




### Python Documentation
Titeler:  
Available types  
Supported operations i Available types    
strftime() and strptime() Format Codes  
timedelta objects  
https://docs.python.org/3.13/library/datetime.html#datetime.datetime.strftime

https://docs.python.org/3/library/datetime.html

https://docs.python.org/3.13/library/datetime.html#format-codes



## Oppgave 4
desverre klarte jeg ikke å fullføre hele oppgave 4, klarte komme meg fram til 4.1 og 4.2.


### Python Documentation
https://docs.python.org/3/library/csv.html#module-csv







## Bruk av KI
Når jeg har brukt KI så prøver jeg å ikke få kode tilbake men med hints på hvordan jeg den logsike måten bør se ut.  

Her så brukte jeg Ki
```
  while True:
        text_input = input("Skriv en text:")
        if text_input == "":
            print("Tom tekst er ugyldig, skriv på nytt med ord")
        elif text_input.isspace():
            print("Bare mellom rom i teksten er ugyglid, skriv på nytt med ord")
       else:
           break
```


```
The logic is basically correct. The first thing I’d check is your indentation.
Look closely here:
elif text_input.isspace(): print("Bare mellom rom i teksten er ugyglid, skriv på nytt med ord")   else:       break

Hint
In Python, if, elif, and else that belong together must all be aligned at the same indentation level.
Think of it like:
if ...
elif ...
else ...

Then the code inside each one is indented one level further.
Also, your logic means:
- "" → loop again
- "    " → loop again
- "hello" → reaches else → break
So your conditions themselves make sense.
Try fixing the indentation around else: first. If it still behaves strangely, send me what happens when you enter something like "hello" and we can trace the loop together.

````

Oppgave 2  

Oppgave 3  

Oppgave 4




## GitHub
Her har jeg laget oppgavene i en git repository sånn jeg kan gjøre commit og push sånn at alle kan se koden min.    
https://github.com/nystrom88/Arbeidskrav-1-Python/tree/main


## Google søk
sort dictionary by value python descending.    

how add data to a list python.  

if my input is minutes how can i display that in hours. 

python how to check if a number can be divided by 3.  

how to reverse text in python.  

how to use lambda function in python.

if a word is true how can i check that python.

IndentationError: expected an indented block after 'if' statement.

how to make a function loop itself if the answer is wrong.  

how to display information from a dict in python.

input days in python with datetime lib.  

how to input a date in python.  

what is strftime.  

what is strptime.  

how to not print the year in timedelta. 

try and except.  

python how to round to 1 decimals. 

what does dictreader do in python.

what is csv dictreader in python

close csv file python safe

print out data from csv file python

## Python Documentation
https://docs.python.org/3/library/decimal.html

https://docs.python.org/3/library/datetime.html

https://docs.python.org/3.13/library/datetime.html#format-codes

https://docs.python.org/3/library/csv.html#module-csv



## Youtube
Python Functions - Visually Explained:
https://www.youtube.com/watch?v=KW6qncswzHw&t=606s  

Learn Python in 1 hour! 🐍:
https://www.youtube.com/watch?v=8KCuHHeC_M0&t=4s  

Python Lambda Functions Explained:
https://www.youtube.com/watch?v=HQNiSfb795A

Learn Python DATES & TIMES in 6 minutes! 📅:
https://www.youtube.com/watch?v=DwBDHsdX6XQ  

Python Tutorial: Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones:
https://www.youtube.com/watch?v=eirjjyP2qcQ

Python Tutorial: CSV Module - How to Read, Parse, and Write CSV Files:
https://www.youtube.com/watch?v=q5uM4VKywbA&t=233s

CSV Files - Visually Explained
https://www.youtube.com/watch?v=PiO2dDvMiJo

``Python Tutorial: if __name__ == '__main__'``:
https://www.youtube.com/watch?v=sugvnHA7ElY

``if __name__ == '__main__' for Python beginners 📥``:
https://www.youtube.com/watch?v=8A0E1dSyjFM




## w3school
https://www.w3schools.com/python/python_lambda.asp
https://www.w3schools.com/python/python_functions.asp  
https://www.w3schools.com/python/python_arguments.asp  
https://www.w3schools.com/python/python_datetime.asp
https://www.w3schools.com/python/python_conditions.asp
https://www.w3schools.com/python/python_lists.asp
https://www.w3schools.com/python/python_datatypes.asp



## Gokstad hjmme siden
https://lms.gokstadakademiet.no/course/view.php?id=483  

