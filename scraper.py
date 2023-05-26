
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


def scraperProccess1():

    array = [ 
        "https://twitter.com/startupyworld", 
        "https://twitter.com/_buildspace",
        "https://twitter.com/_Glasp"
    ]

    chromedriver = ChromeDriverManager().install()
    driver = webdriver.Chrome(chromedriver)

    listOfTweets = []

    for url in array:
        driver.get(url)
        time.sleep(4)
        tweets = driver.find_elements(By.XPATH, '//*[@data-testid="tweet"]')

        # Print out the text of each element
        for tweet in tweets:
            timeElementText = tweet.find_element(By.TAG_NAME, "time").text

            # check if the tweet was in the last day
            # if "h" in timeElementText:
            
            tweetName = tweet.find_elements(By.XPATH, './/*[@data-testid="User-Name"]')

            tweetContent = tweet.find_elements(By.XPATH, './/*[@data-testid="tweetText"]')

            string = ""
            for x in tweetContent:
                string = string + x.text
            

            tweetObject = {
                "name": tweetName[0].text,
                "tweetContent": string,

            }

            listOfTweets.append(tweetObject)
            print(tweetObject)
    
    return(listOfTweets)



def scraperProccess2():

    array = [ 
        "https://twitter.com/paulg", 
        "https://twitter.com/gaby_goldberg",
        "https://twitter.com/lennysan",
        "https://twitter.com/dwr",
        "https://twitter.com/sama",
    ]

    chromedriver = ChromeDriverManager().install()
    driver = webdriver.Chrome(chromedriver)

    listOfTweets = []

    for url in array:
        driver.get(url)
        time.sleep(4)
        tweets = driver.find_elements(By.XPATH, '//*[@data-testid="tweet"]')

        # Print out the text of each element
        for tweet in tweets:
            timeElementText = tweet.find_element(By.TAG_NAME, "time").text

            # check if the tweet was in the last day
            if "h" in timeElementText:
            
                tweetName = tweet.find_elements(By.XPATH, './/*[@data-testid="User-Name"]')

                tweetContent = tweet.find_elements(By.XPATH, './/*[@data-testid="tweetText"]')

                string = ""
                for x in tweetContent:
                    string = string + x.text
                

                tweetObject = {
                    "name": tweetName[0].text,
                    "tweetContent": string,

                }

                listOfTweets.append(tweetObject)
                print(tweetObject)
    
    return(listOfTweets)
