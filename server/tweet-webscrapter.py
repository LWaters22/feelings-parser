from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://twitter.com/MULANEY?lang=en'

# 'https://twitter.com/' + mulaney + "?lang=en'
# 'https://twitter.com/BarackObama?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
# 'https://twitter.com/TheEllenShow?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
# 'https://twitter.com/KevinHart4real?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
# 'https://twitter.com/mulaney?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
# 'https://twitter.com/amyschumer?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'

uClient = uReq(my_url)
page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

tweets = page_soup.findAll("div", {"class":"tweet", "data-screen-name":"mulaney"})

# print("tweets: ", tweets)

for tweet in tweets:
  # full name
  fullname = tweet.find('strong', {"class":"fullname"}).text
  # time posted
  time_posted = tweet.find('a', {"class":"tweet-timestamp"})["title"]
  # tweet text
  tweet_content = tweet.find('p', {"class":"tweet-text"})
  # if len(tweet_content.findAll('a')) > 1:
  #   tweet_content.findAll('a')[1].extract()
  tweet_text = tweet_content.text

  print(fullname, time_posted, tweet_text + "\n")
  # with all extra data: page_soup.find('p', {"class":"tweet-text"})

