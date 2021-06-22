from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from article_outline import ArticleOutline
from firebase_service import FirebaseService

# def fetchArticleOutline(driver,index):
#     global firebaseService

#     data = None
#     while type(data) is not WebElement:
#         try:
#             data = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, f"div[data-index='{index-1}']")))
#         except:
#             html = driver.find_element_by_tag_name("html")
#             html.send_keys(Keys.PAGE_DOWN)

#     try:
#         article = WebDriverWait(data,1).until(EC.presence_of_element_located((By.XPATH, f"./article")))
#     except:
#         return

#     try:
#         title = WebDriverWait(article,5).until(EC.presence_of_element_located((By.XPATH, f"./h2/a/span")))

#         link = WebDriverWait(article,5).until(EC.presence_of_element_located((By.XPATH,f"./h2/a")))
        
#         emoji_amount = WebDriverWait(article,5).until(EC.presence_of_element_located((By.XPATH,f"./div[3]/div[1]/div/div[2]")))
        
#         reply_amount = WebDriverWait(article,5).until(EC.presence_of_element_located((By.XPATH,f"./div[3]/div[2]/div/span")))

#         articleOutline = ArticleOutline(title.text, link.get_attribute("href"),emoji_amount.text,reply_amount.text)
        
#         articleOutline.printArticleOutline()

#         # firebaseService.addArticleOutline(articleOutline)
#     except:
#         return

def crawl():
    chorme_options = webdriver.ChromeOptions()
    chorme_options.add_argument("--headless")
    chorme_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=chorme_options)
    driver.get("https://sites.google.com/g.ncu.edu.tw/rchmp")

    title = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[1]/section[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/p[1]/span/a")))

    print(title.text)

    link = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[1]/section[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/p[1]/span/a")))

    print(link.get_attribute("href"))

    date = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[1]/section[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/p[1]/span/a")))

    print(date.text)

    driver.quit()


if __name__ == "__main__":
    # firebaseService = FirebaseService()
    # firebaseService.fetchData()
    crawl()
