from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def getAppleRating():

    driver = webdriver.Chrome()

    driver.get("https://apps.apple.com/us/app/everyday/id1338702323")

    driver.implicitly_wait(10)

    appleRating = driver.find_element(by=By.XPATH, value="/html/body/div[3]/main/div[2]/section[1]/div/div[2]/header/ul[1]/li/ul/li/figure/figcaption").text.split()[0]

    return appleRating



def getGoogleRating():

    driver = webdriver.Chrome()

    driver.get("https://play.google.com/store/apps/details?id=com.dynamify.sodexo&hl=en_US&gl=US")

    driver.implicitly_wait(10)

    googleRating = driver.find_element(by=By.XPATH, value="/html/body/c-wiz[2]/div/div/div[2]/div[1]/div/div/c-wiz/div[2]/div[2]/div/div/div[1]/div[1]/div/div").text.split()[0]

    return googleRating

def main():

    x = 1

    data = [getAppleRating(),getGoogleRating()]

    dfData = pd.DataFrame(data,columns=["Apple Rating", "Google Rating"])

    print(dfData)

if __name__ == "__main__":
    main()

