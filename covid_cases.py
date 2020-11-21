import csv
import wget
import datetime

day = datetime.datetime.now().day
month = datetime.datetime.now().month
year = datetime.datetime.now().year
date = str(month) + "-" + str(day) + "-" + str(year)
link = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + date + ".csv"

while True:
    print("\n" + date)
    try:
        try:
            open(date)
        except:
            wget.download(link, date)
    except Exception as ex:
        day = day - 1
        date = str(month) + "-" + str(day) + "-" + str(year)
        link = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + date + ".csv"
    else:
        break

print("\n")

while True:
    file = open(date)
    reader = csv.reader(file)
    region = input("Enter province or country: ")
    if region == "exit" or region == "EXIT":
        break
    for row in reader:
        if(region == row[2] or region == row[3]):
            print("**************************************")
            print("Province: ", row[2])
            print("Country: ", row[3])
            print("Confirmed: ", row[7])
            print("Deaths: ", row[8])
            print("Recovered: ", row[9])
            print("Active: ", row[10])
            print("**************************************\n")
