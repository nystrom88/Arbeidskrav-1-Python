import csv
from itertools import count


def get_data():
    with open("supporthenvendelser (3).csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def fix_data(data_list):
    correct_data = []
    mistake_data = []

    for row, data in enumerate(data_list):
        row += 1
        is_correct = True

        try:
            # id
            id_row = int(data["id"])
            if id_row < 0:
                mistake_data.append(
                    f"Feil i rad {row}, feil i kolone ID verdien er {data["id"]}, id skal være posetiv hel tall")
                is_correct = False
        except ValueError:
            mistake_data.append(
                f"Feil i rad {row}, feil i kolone ID verdien er {data["id"]}, id skal være posetiv hel tall")
            is_correct = False

        try:
            # minutte
            minute = int(data["minutes"])
            if minute < 0:
                mistake_data.append(
                    f"Feil i rad {row}, feil i kolone Minutter verdien er {data["minutes"]}, skal være posetiv hel tall")
                is_correct = False
        except ValueError:
            mistake_data.append(
                f"Feil i rad {row}, feil i kolone Minutter verdien er {data["minutes"]}, skal være posetiv hel tall")
            is_correct = False

        try:
            # category
            if data["category"] == "":
                mistake_data.append(
                    f"Feil i rad {row}, feil i kolonen Category verdien er {data["category"]}, skal ha en kategori")
                is_correct = False
        except ValueError:
            mistake_data.append(
                f"Feil i rad {row}, feil i kolonen Category verdien er {data["category"]}, skal ha en kategori")
            is_correct = False

        try:
            # is resolved
            if data["is_resolved"] not in ("yes", "no"):
                mistake_data.append(
                    f"Feil i rad {row}, feil i kolone Resolved verdien er {data["is_resolved"]}, skal være Yes eller No")
                is_correct = False
        except ValueError:
            mistake_data.append(
                f"Feil i rad {row}, feil i kolone Resolved verdien {data["is_resolved"]}, skal være Yes eller No")
            is_correct = False

        if is_correct == True:
            correct_data.append(data)

    return correct_data, mistake_data


def total_issues(data_list):
    return len(data_list)

def data_per_category(data_list):
    count_category = {}

    for x in data_list:
        category = x["category"]
        if category not in count_category:
           count_category[category] = 0

        count_category[category] += 1

    return count_category

def total_time(data_list):
    total_minutes = 0
    for x in data_list:
        minuter = int(x["minutes"])
        total_minutes = minuter + total_minutes
    return total_minutes

def average_time(data_list, total_minutes):
    average_total_time = total_minutes / len(data_list)
    average_total_time = round(average_total_time, 1)
    return average_total_time


def resolved_data(data_list):
    count_yes = {}

    for x in data_list:
        resolved = x["is_resolved"]
        if resolved not in count_yes:
            count_yes[resolved] = 0

        count_yes[resolved] += 1

    return count_yes

def most_asked_category(data_list):
    count_category = {}


    for x in data_list:
        category = x["category"]
        if category not in count_category:
            count_category[category] = 0

        count_category[category] += 1

    high_value = 0
    high_category = ""

    for category, value in count_category.items():
        if value > high_value:
            high_value = value
            high_category = category

    return f"{high_category} har flest med {high_value}"

def unresolved_sorted(data_list):
    unresolved = []

    for issue in data_list:
        if issue["is_resolved"] == "no":
            row = [
                int(issue["minutes"]),
                issue["id"],
                issue["category"]
            ]
            unresolved.append(row)

    unresolved = sorted(unresolved, reverse=True)

    for row in unresolved:
        print(f"ID: {row[1]}, kategori: {row[2]}, minutter: {row[0]} minutter")
    return unresolved



def main():
    data = get_data()
    corrected_data_list, mistake_data_list = fix_data(data)
    total_issues_length = total_issues(corrected_data_list)
    per_category = data_per_category(corrected_data_list)
    total_minutes = total_time(corrected_data_list)
    average_minutes = average_time(corrected_data_list, total_minutes)
    resolved_count = resolved_data(corrected_data_list)
    most_asked = most_asked_category(corrected_data_list)
    unresolved_by_minute_length = unresolved_sorted(corrected_data_list)



if __name__ == '__main__':
    main()