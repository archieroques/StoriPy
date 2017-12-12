import tweepy
import datetime

now = datetime.datetime.now()
cyear = str(now.year)
cmonth = str(now.month)
cday = str(now.day)


name = "StoriPy_" + cyear + cmonth + cday + ".txt"
file = open(name,"w+")

key = "Your Consumer Key (API key) here"
sekretz = "Your Consumer Secret (API Secret) here"

auth = tweepy.OAuthHandler(key, sekretz)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#makershour', rpp=100).items():
    year, month, day = str(tweet.created_at).split("-")
    day = day[:2]
    if day == cday and month == cmonth and year == cyear:
        tweetText = (tweet.text).encode("utf-8")
        tweetText = str(tweetText, errors='ignore')
        tweetURL = 'https://twitter.com/i/status/' + tweet.id_str

        file.write((tweetURL+ "\n"))
        try:
            print(tweetURL, " ", tweetText)
        except UnicodeEncodeError:
            pass
        print()
    else:

        file.close()
        break
