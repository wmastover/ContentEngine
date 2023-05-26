from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from scraper import scraperProccess2
from getJSON import getJSON
import json
from gptAPICalls import getOneLine



def convert_to_json(obj):
    return json.dumps(obj, default=lambda x: x.__dict__)

FrontdoorDescription = " Frontdoor is a tech startup looking to change the internet. We are doing this by focusing on the use of curation and AI to optimise the user experience. "

FrontdoorTweetList = getJSON("FrontdoorTweets.json")

ContextTweetList = convert_to_json(scraperProccess2())


Messages =  [
    {
      "role": "system",
      "content": "You are a creative AI model tasked with generating first drafts of tweets for a company. Your goal is to create engaging, informative, and relevant content that aligns with the company's brand and resonates with its audience."
    },
    {
      "role": "user",
      "content": "Here is some information about my company:" + FrontdoorDescription
    },
    {
      "role": "user",
      "content": "Here are some of our previous tweets: " +  FrontdoorTweetList
    },
    {
      "role": "user",
      "content": "Here are some tweets from relevant companies that do well on Twitter: " + ContextTweetList
    },
    {
      "role": "user",
      "content": "Based on this information, please generate 10 relevant tweets for our company, focusing on the topics of:  Curation, AI, and Second Brains. Return these in JSON format."
    }
  ]



getOneLine(Messages)
