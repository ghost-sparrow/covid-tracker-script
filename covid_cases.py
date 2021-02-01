#!/bin/python3
import datetime
import csv
import wget

#Get the current date
day = datetime.datetime.now().day
Month = datetime.datetime.now().month
Year = datetime.datetime.now().year

#The database of a certain day is saved as its date.
#For example, a database of 21st November 2020 will be saved as 11-21-2020
date = str(Month) + "-" + str(day) + "-" + str(Year)

def decremeant_date(dy, mnth, yr):
    if(dy == 1):
        dy = 31
        if(mnth == 1):
            mnth = 12
            yr = yr-1
            return [dy, mnth, yr]
        mnth = mnth - 1
        return [dy, mnth, yr]
    dy = dy - 1
    return [dy, mnth, yr]

#Link from where to download the file
link = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/"\
"master/csse_covid_19_data/csse_covid_19_daily_reports/" + date + ".csv"

#Get the latest database
while True:
    print("\n" + date)
    try:
        try:
            #If a file of a certain date is already downloaded, there is no need to download it again
            open(date)
        except Exception as open_error:
            #If error occured opeing the file, download the file
            print("No downloaded database. Downloading now...")
            wget.download(link, date)
            print("Download complete!")
    except Exception as download_error:
        #If error occured downloading the file, decreament the day and generate a new date and link
        day, Month, Year = decremeant_date(day, Month, Year)
        if(day < 10):
            day_str = "0" + str(day)
        else:
            day_str = str(day)
        if(Month < 10):
            Month_str = "0" + str(Month)
        else:
            Month_str = str(Month)
        date = Month_str + "-" + day_str + "-" + str(Year)
        link = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/"\
        "master/csse_covid_19_data/csse_covid_19_daily_reports/" + date + ".csv"
        print('No database for the given date exists. Decrementing date.')
    else:
        #If everything works fine, continue to the program
        break

print("\n")

while True:
    #Open the file and csv reader
    file = open(date)
    reader = csv.reader(file)
    
    #Get user input
    region = input("Enter province or country: ")
    
    #Find and print data matching the input
    if region in ("exit", "EXIT"):
        break
    for row in reader:
        if region in(row[2], row[3]):
            print("**************************************")
            print("Province: ", row[2])
            print("Country: ", row[3])
            print("Confirmed: ", row[7])
            print("Deaths: ", row[8])
            print("Recovered: ", row[9])
            print("Active: ", row[10])
            print("**************************************\n")
