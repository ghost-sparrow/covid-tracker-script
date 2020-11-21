import datetime
import csv
import wget

day = datetime.datetime.now().day
Month = datetime.datetime.now().month
Year = datetime.datetime.now().year
date = str(Month) + "-" + str(day) + "-" + str(Year)
link = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/"\
"master/csse_covid_19_data/csse_covid_19_daily_reports/" + date + ".csv"

while True:
    print("\n" + date)
    try:
        try:
            open(date)
        except Exception as open_error:
            print("No downloaded database. Downloading now...")
            wget.download(link, date)
            print("Download complete!")
    except Exception as download_error:
        day = day - 1
        date = str(Month) + "-" + str(day) + "-" + str(Year)
        link = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/"\
        "master/csse_covid_19_data/csse_covid_19_daily_reports/" + date + ".csv"
    else:
        break

print("\n")

while True:
    file = open(date)
    reader = csv.reader(file)
    region = input("Enter province or country: ")
    if region in ("exit", "EXIT"):
        break
    for row in reader:
        if(region in(row[2], row[3])):
            print("**************************************")
            print("Province: ", row[2])
            print("Country: ", row[3])
            print("Confirmed: ", row[7])
            print("Deaths: ", row[8])
            print("Recovered: ", row[9])
            print("Active: ", row[10])
            print("**************************************\n")
