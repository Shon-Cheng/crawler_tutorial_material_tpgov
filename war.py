from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

def printcrawl(driver,index):
    data = None
    while type(data) is not WebElement:
        try:
            data = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, f"div[class='{index-panel panel-default}']")))
        except:
            html = driver.find_element_by_tag_name("html")
            html.send_keys(Keys.PAGE_DOWN)

    try:
        article = WebDriverWait(data,1).until(EC.presence_of_element_located((By.XPATH, f"./article")))
    except:
        return

    try:
        title = WebDriverWait(article,5).until(EC.presence_of_element_located((By.XPATH, f"./h2/a/span")))
        print(title.text)

        link = WebDriverWait(article,5).until(EC.presence_of_element_located((By.XPATH,f"./h2/a")))
        print(link.get_attribute("href"))

        emoji_amount = WebDriverWait(article,5).until(EC.presence_of_element_located((By.XPATH,f"./div[3]/div[1]/div/div[2]")))
        print(emoji_amount.text)

        reply_amount = WebDriverWait(article,5).until(EC.presence_of_element_located((By.XPATH,f"./div[3]/div[2]/div/span")))
        print(reply_amount.text)
    except:
        return

def crawl():
    chorme_options = webdriver.ChromeOptions()
    # chorme_options.add_argument("--headless")
    chorme_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=chorme_options)
    driver.get("https://www.ncdr.nat.gov.tw/Frontend/Prevention/General?Type=38")

    for i in range(2,50):
        printcrawl(driver,i)

    driver.quit()


if __name__ == "__main__":
    crawl()