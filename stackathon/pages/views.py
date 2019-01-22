from bs4 import BeautifulSoup as soup
from django.shortcuts import render
from django.views.generic import View
from urllib.request import urlopen as uReq
import json

from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six

class FrontendRenderView(View):
  def get(self, request, *args, **kwargs):
    print('successfully in FrontendRenderView')

    my_url = 'https://twitter.com/barackobama?lang=en'

    # 'https://twitter.com/' + mulaney + "?lang=en'
    # 'https://twitter.com/' + username + "?lang=en'

    uClient = uReq(my_url)
    page_html = uClient.read()

    uClient.close()

    page_soup = soup(page_html, "html.parser")

    profileHeader = page_soup.find("div", {"class": "ProfileHeaderCard"})

    username = profileHeader.find("b", {"class":"u-linkComplex-target"}).text
    fullname = profileHeader.find("a", {"class":"ProfileHeaderCard-nameLink"}).text
    avatar = page_soup.find("img", {"class":"ProfileAvatar-image"})["src"]

    tweets = page_soup.findAll(
        "div", {"class": "tweet", "data-screen-name": username})

    tweet_array = []
    analysis_array = []

    counter = 0
    for tweet in tweets:
      if (counter > 9):
        break
      # tweet text
      tweet_content = tweet.find('p', {"class": "tweet-text"})
      # if len(tweet_content.findAll('a')) > 1:
      #   tweet_content.findAll('a')[1].extract()
      tweet_text = tweet_content.text

      # analysis = sample_analyze_sentiment(tweet_text)

      tweet_array.append(tweet_text)

      # analysis_array.append(analysis)
      counter += 1

    context = {
      'username': username,
      'fullname': fullname,
      'avatar': avatar,
      'num_tweets': len(tweet_array),
      'tweet_array': tweet_array,
      # 'analysis_array': analysis_array
    }

    return render(request, "index.html", context=context)

  def post(self, request, *args, **kwargs):
    print("posting!")




def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    # content = 'Your text to analyze, e.g. Hello, world!'

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    return ['Score: {}'.format(sentiment.score), 'Magnitude: {}'.format(sentiment.magnitude)]
