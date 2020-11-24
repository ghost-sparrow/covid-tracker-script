# covid-tracker-script
A simple python script to fetch the latest covid info

## How it works
1) First, get the current date in MM-DD-YYYY format.
2) Check if the csv database for that file has been downloaded. If not, download it using wget from [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports).
3) If wget returns error, decreament the day by one.
4) Go back to step 2 until th latest covid info has been downloaded.
5) Open the file with csv reader.
6) Ask the user for input of a province or a country.
7) If a province or a country exists, then print the latest covid info of that place. If not, print nothing.
8) Go back to step 6 until the user gives interrupt or gives `exit` as province.

## NOTE
PLease make sure to install the pip python module before running the script.
### Windows
1) Run command prompt as administrator.
 - Go to Start > Windows System > Right click on command prompt and run as administrator.
OR
 - Press Windows Key + R and press cmd. Then press Ctrl + Shift + Enter.
2) Execute `pip install wget`.
