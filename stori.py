import tweepy
import datetime

now = datetime.datetime.now()
cyear = str(now.year)
cmonth = str(now.month)
cday = str(now.day)

searchTerm = "#makershour"
name = "StoriPy_" + cyear + cmonth + cday + ".txt"
file = open(name,"w+")

the_tweets = []

key = "Your Consumer Key (API key) here"
sekretz = "Your Consumer Secret (API Secret) here"

auth = tweepy.OAuthHandler(key, sekretz)
api = tweepy.API(auth)

print("Finding tweets from today's date containing the word or phrase '", searchTerm, "'.")

for tweet in tweepy.Cursor(api.search, q=searchTerm, rpp=100).items():
    year, month, day = str(tweet.created_at).split("-")
    day = day[:2]
    if day == cday and month == cmonth and year == cyear:
        tweetText = (tweet.text).encode("utf-8")
        tweetText = str(tweetText, errors='ignore')
        tweetURL = 'https://twitter.com/i/status/' + tweet.id_str

        the_tweets.append(tweetURL)
        #file.write((tweetURL+ "\n"))
        try:
            print(tweetURL, " ", tweetText)
        except UnicodeEncodeError:
            pass
        print()
    else:
        #print(year, cyear, month, cmonth, day, cday)
        break

print("Writing to file...")
the_tweets.reverse()

for item in range(len(the_tweets)):
    file.write(the_tweets[item] + "\n")

    
file.close()
print("Done! Tweet URLs written to file ", name, ". Have a nice day!")
