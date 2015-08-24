#coding:utf-8
__author__ = 'Administrator'
#TASK9#
#mutiple Thread#
import time,threading
import requests
import sys
import re
reload(sys)
sys.setdefaultencoding("utf-8")
# def loop():
#     print'thread %s is running...' % threading.current_thread().name
#     n=0
#     while n<5:
#         n=n+1
#         print 'thread %s>>>%s' % (threading.current_thread().name,n)
#         time.sleep(1)
#     print'thread %s is running....' %threading.current_thread().name
#     t=threading.Thread(target=loop,name='LoopThread')
#     t.start()
#     t.join()
#     print'thread %s ended' % threading.current_thread().name
# loop()
#hea={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'}
#html=requests.get('http://www.baidu.com',headers = hea)
#html=requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python')
#html=requests.get('http://www.uestc.edu.cn')
#url='http://www.uestc.edu.cn'
class DownloadThread(threading.Thread):
#getsource用来获取网页源代码
    urls=[]
    n=1
    def run(self):  # Overwrite method, here we can do something we want in the thread
       self.saveinfo()
    def getsource(self,url):
        html = requests.get(url)
        html.encoding = 'utf-8'
        return html.text
    def geteveryurl(self,sources):
        everyurl = re.findall('href="http://www.*?"',sources,re.S)
        self.urls=everyurl
        return everyurl
    def saveinfo(self):
        text=self.getsource('http://www.uestc.edu.cn')
        self.geteveryurl(text)
        for url in self.urls:
           # if self.n>5:
           #     break
           newurl=url[6:-1]
           print"正在下载第"+str(self.n)+"个网页："+newurl
           string='web'+ str(self.n) +'.html'
           f = open(string,'a')
           text=self.getsource(newurl)
           f.write(text)
           f.close()
           self.n=self.n+1
#print html.text


thread1 = DownloadThread()
thread2 = DownloadThread()
thread1.start()
thread2.start()