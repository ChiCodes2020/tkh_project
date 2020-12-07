from app import db, TweetTable
import requests
from bs4 import BeautifulSoup


tweet_data = [] 

def scrape():
    req = requests.get('https://nitter.net/drthema')
    soup = BeautifulSoup(req.text) 
    all_divs = soup.find_all("div", {"class": "tweet-body"})
    

    
    for i in all_divs:
        tweet_div = i.find("div", {"class": "tweet-content media-body"})

        tweets = tweet_div.text
        
    
        spans = i.find_all("span", {"class": "tweet-stat"})

        likes = spans[3].text
        
   
        tweet_data.append([tweets, likes])
    
            
# scrape()
    return tweet_data

# set up your scraping below




# this `main` function should run your scraping when 
# this script is ran.
def main():
    tweet_data = scrape()
    db.drop_all()
    db.create_all()
    for tweets in tweet_data:
        print(tweets)
        new_row = TweetTable(tweets=tweets[0], likes=tweets[1])
        print(new_row)
        db.session.add(new_row)
        db.session.commit()

if __name__ == '__main__':
    main()