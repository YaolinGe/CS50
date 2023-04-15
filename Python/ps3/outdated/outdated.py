months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def get_date(): 
    """ Get the date in the format of month/day/year """

    while True: 
        date = input("Date: ").strip()
        if date.count("/") == 2: 
            month, day, year = date.split("/")
            if month.isdigit() and day.isdigit() and year.isdigit(): 
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year <= 2099: 
                    return month, day, year
        elif "," in date:
            md, year = date.split(",")
            month, day = md.split(" ")
            year = year.strip()
            if month.title() in months and day.isdigit() and year.isdigit(): 
                month = months.index(month) + 1
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year <= 2099:
                    return month, day, year
    

def main():
    month, day, year = get_date()
    print(f"{year:4d}-{month:02d}-{day:02d}")


if __name__ == "__main__":
    main()