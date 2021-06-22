# 抓取NCU災害防治中心的網頁原始碼(HTML)
import urllib.request as req
url="https://www.dcard.tw/f"
# 建立一個Request 物件，附加Request Headers的資訊
# (讓自己看起來比較像人類來探訪)
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("UTF-8")
# 解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("h2", class_="tgn9uw-2 jWUdzO")  # 尋找所有 class="aw5Odc" 的 span 標籤    
for title in titles:
    print(title.a.string)