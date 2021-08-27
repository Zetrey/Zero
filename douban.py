from urllib.parse import urlencode
import urllib.request,urllib.error
from bs4 import BeautifulSoup
import urllib.request,urllib.error

def main():
    baseurl = "https://movie.douban.com/top250?start="
    daralist=getData(baseurl)
    savepath=".\\TOP250.xls"
    askURL("https://movie.douban.com/top250?start=")

def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)
    return datalist

def askURL(url):
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
    }
    requst = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(requst)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def saveData(savepath):
    print("save....")



if __name__ == "__main__":
    main()















'''
#beautifulsoup 将html文档转换成一个树形结构，
from bs4 import BeautifulSoupdef main():
    baseurl = "https://movie.douban.com/top250?starts=;"
    #获取
    datalist = getspdier(baseurl)
    #保存
    savepath = ".\\豆瓣电影TOP250.xls"  #。表示当前文件夹
    #savespdier(savepath)#2获取爬取内容并解析
def getspdier(bassurl):
    datalist = []
    for i in range(0,10):
        url = bassurl + str(i*25) #总共爬取250个
        html = askURL(url) #保存获取的网页源码

        #逐一解析

    return datalist

#获取单个URL的网页内容
def askURL(url):
    headers = {User-Agent...}
    #封装信息
    request = urllib.request.Request(url,headers = headers)
    html = 
    try:
        #接收的封装对象
        response = urllib.request.urlopen(request)
        html = response.read().decode(utf-8) #decode 解码
        print(html)
    except  Exception as e:
        if hasattr(e,code):
            print(e.code)
        if hasattr(e,原因):
            print(e.reason)
    return html
'''