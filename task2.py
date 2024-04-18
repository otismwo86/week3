import urllib.request as req
import csv
rows=[]
url="https://www.ptt.cc/bbs/Lottery/index.html"
def getdata(url):
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    for title in titles:
            if title.a != None:
                title_text=title.a.string
                link=title.a.get('href')
                pagelink="https://www.ptt.cc"+link
                request1=req.Request(pagelink,headers={
                    "cookie":"over18=1",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
                })
                with req.urlopen(request1) as response1:
                    data1=response1.read().decode("utf-8") 
                root1=bs4.BeautifulSoup(data1, "html.parser")
                titles1=root1.find_all("span",class_="article-metaline") #method 0
                time_elements=root1.select('.article-meta-value')
                if len(time_elements)>=4:
                    target_string=time_elements[3].text
                nrec_span=title.find_previous_sibling(class_="nrec")
                if nrec_span and nrec_span.span != None:
                    nrec=nrec_span.span.string
                else:
                    nrec="0"
                rows.append([title_text,nrec,target_string]) 
    nextlink=root.find("a",string="‹ 上頁")
    return nextlink["href"]
pageurl="https://www.ptt.cc/bbs/Lottery/index.html"
n=0
while n<3:
    pageurl="https://www.ptt.cc"+getdata(pageurl)
    n+=1


with open("article.csv", "w", newline="", encoding="utf-8") as file:
    data2 = csv.writer(file)
    data2.writerows(rows)

