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

    return render(request, "index.html", {})

class getAnalysis(View):
  def get(self, request, search_username, **kwargs):
    print('successfully in FrontendRenderView')
    print(search_username)

    my_url = 'https://twitter.com/' + search_username + '?lang=en'

    uClient = uReq(my_url)
    page_html = uClient.read()

    uClient.close()

    page_soup = soup(page_html, "html.parser")

    tweets = page_soup.findAll(
      "div", {"class": "tweet", "data-screen-name": search_username})

    tweet_array = []
    analysis_array = []

    counter = 0
    for tweet in tweets:
      if (counter > 9):
        break
      # tweet text
      tweet_content = tweet.find('p', {"class": "tweet-text"})
      tweet_text = tweet_content.text

      analysis = sample_analyze_sentiment(tweet_text)
      # print(analysis)
      tweet_array.append(tweet_text)

      analysis_array.append(analysis)
      counter += 1

    analysis_array = ', '.join(analysis_array)
    print(analysis_array)

    context = {
      'tweet_array': tweet_array,
      'analysis_array': analysis_array
    }

    return render(request, "analysis.html", context=context)

class postUsername(View):
  def get(self, request, search_username, **kwargs):
    print('successfully in FrontendRenderView')
    print(search_username)

    my_url = 'https://twitter.com/' + search_username + '?lang=en'

    uClient = uReq(my_url)
    page_html = uClient.read()

    uClient.close()

    page_soup = soup(page_html, "html.parser")

    profileHeader = page_soup.find("div", {"class": "ProfileHeaderCard"})

    username = profileHeader.find("b", {"class":"u-linkComplex-target"}).text
    fullname = profileHeader.find("a", {"class":"ProfileHeaderCard-nameLink"}).text
    avatar = page_soup.find("img", {"class":"ProfileAvatar-image"})["src"]


    context = {
      'username': username,
      'fullname': fullname,
      'avatar': avatar,
    }

    return render(request, "content.html", context=context)

def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    # content = 'Your text to analyze, e.g. Hello, world!'

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    print('in analysis method', sentiment.score, sentiment.magnitude)
    if (sentiment.score > .3):
      return 'positive'
    elif(sentiment.score < (-.3)):
      return 'negative'
    elif(sentiment.magnitude > .3):
      return 'mixed'
    else:
      return 'neutral'
