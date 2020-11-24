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
        day = day - 1
        date = str(Month) + "-" + str(day) + "-" + str(Year)
        link = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/"\
        "master/csse_covid_19_data/csse_covid_19_daily_reports/" + date + ".csv"
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
