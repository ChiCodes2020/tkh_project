import requests
from bs4 import BeautifulSoup
import csv

#we want to create a script in python
#we want to create a function that scrapes from the specified website
covid_data = [["Country", "Cases", "Deaths", "Recoveries", "Death_rate", "Recovery_rate" ]] 

def scrape():
    req = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data')
    soup = BeautifulSoup(req.text) #or req.context
    for i in soup.select("tr")[2:]: 
        try:
            country_name = list(i.select("th")[1].strings)[0]
            country = country_name[0]
#             
            
            country_cases = list(i.select("td")[0].strings)[0]
            if country_cases == "No data":
                country_cases = None
            else:
                country_cases = int(country_cases.replace(",",""))
            
            
            country_deaths = list(i.select("td")[1].strings)[0]
            if country_deaths == "No data":
                country_deaths = None
            else:
                country_deaths = int(country_deaths.replace(",",""))
            
            
            country_recoveries = list(i.select("td")[2].strings)[0]
            if country_recoveries == "No data":
                country_recoveries = None
            else:
                country_recoveries = int(country_recoveries.replace(",",""))
            
            
            
            death_rate = None
            recovery_rate = None
            

   
            if country_cases and country_deaths:
                death_rate = country_deaths /(country_cases)
                
                
            if country_cases and country_recoveries:
                 recovery_rate = country_recoveries / (country_cases)
            
            country_data = [country_name, country_cases, country_deaths, country_recoveries, death_rate,recovery_rate]
            covid_data.append(country_data)
            
        except IndexError:
            break
    
        
    return covid_data
    
