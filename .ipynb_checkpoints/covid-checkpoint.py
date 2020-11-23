import requests
from bs4 import BeautifulSoup
import csv

#we want to create a script in python
#we want to create a function that scrapes from the specified website
covid_data = [["Country", "Cases", "Deaths", "Recoveries", "Death_rate", "Recovery_rate" ]] 

def scrape():
    req = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data')
    soup = BeautifulSoup(req.text)
    for i in soup.select("tr")[2:]: 
        try:
            country_name = list(i.select("th")[1].strings)[0]
#             print(country_name)
            
            country_cases = list(i.select("td")[0].strings)[0][:-1]
            if country_cases == "No dat":
                country_cases = None
            
            country_deaths = list(i.select("td")[1].strings)[0][:-1]
            if country_deaths == "No dat":
                country_deaths = None
            
            country_recoveries = list(i.select("td")[2].strings)[0][:-1]
            if country_recoveries == "No dat":
                country_recoveries = None
               


            
            country_data = [country_name, country_cases, country_deaths, country_recoveries]
            covid_data.append(country_data)
            
        except:
            break
    
        
    return covid_data