import requests
from bs4 import BeautifulSoup
import csv

tweet_data = [["Tweets", "Likes"]] 

def scrape():
    req = requests.get('https://nitter.net/drthema')
    print("hello world")
    soup = BeautifulSoup(req.text) 
    print("hello world")
    all_divs = soup.find_all("div", {"class": "tweet-body"})
    

    
    for i in all_divs:
        tweet_div = i.find("div", {"class": "tweet-content media-body"})
        print( "\n \n TWEET:\n", tweet_div.text)
        tweets = tweet_div.text
        
    
        spans = i.find_all("span", {"class": "tweet-stat"})
        print("Likes =", spans[3].text)
        likes = spans[3].text
        

        
        print("\n \n TWEET:\n",tweet_div.text, "Likes =", spans[3].text )
        
#icon-container   
        tweet_data.append([tweets, likes])
    
            
# scrape()
    return tweet_data

    
if __name__=="__main__":
    output_file = open("Chioma2-scraping-project1.csv", "w")
    write_file = csv.writer(output_file)
    write_file.writerows(scrape())
    output_file.close()
