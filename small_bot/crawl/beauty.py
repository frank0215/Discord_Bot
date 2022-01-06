import requests
from bs4 import BeautifulSoup
import datetime
import random


class Beauty:
    def __init__(self):
        self.arr = []

    '''
    Change the date format xxxx/xx/xx to xxxx-xx-xx
    so that the crawler can crawl the right url successfully.
    '''
    def change_date(self, d):
        if len(d.split('/')) == 3:
            d = '-'.join(d.split('/'))
        return d

    '''
    Get each article url where I can crawl the picture.
    '''
    def getArticle(self, start_date, period=0, cur_page=1):
        today = datetime.datetime.today()
        start_date = self.change_date(start_date)
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        delta_date = today - start_date
        if delta_date.days < 0:
            return None
        end_date = start_date + datetime.timedelta(days=-period)

        url = f'https://www.jkforum.net/forum-736-{cur_page}.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        articles = soup.select('form li')

        isEnd = False
        for article in articles:
            for d1, d2 in zip(article('em'), article('h3')):
                articleInfo = []
                a_date = d1.select_one('span').get('title')
                a_date = datetime.datetime.strptime(a_date, '%Y-%m-%d')
                check_date = a_date - end_date
                if check_date.days < 0:
                    isEnd = True
                    break
                if a_date > start_date or a_date < end_date:
                    continue
                articleInfo.append(datetime.datetime.strftime(a_date, '%Y-%m-%d'))

                articleUrl = 'https://www.jkforum.net/' + d2.select_one('a').get('href')
                articleInfo.append(articleUrl)
                #print(articleUrl)
                articleTitle = d2.select_one('a').text
                articleInfo.append(articleTitle)
                #print(articleTitle)
                self.arr.append(articleInfo)        
            if isEnd:
                break

        if start_date < today and len(self.arr) == 0:
            start_date = datetime.datetime.strftime(start_date, '%Y-%m-%d')
            cur_page += 1
            return self.getArticle(start_date, period, cur_page)
        else:
            if isEnd == False:
                start_date = datetime.datetime.strftime(start_date, '%Y-%m-%d')
                cur_page += 1
                return self.getArticle(start_date, period, cur_page)
            return self.arr

    '''
    Crawl the picture from the given article website
    '''
    def getImgUrl(self, articleList, max_num=0):
        if articleList == None:
            return
        imgList = []

        for i in range(len(articleList)):
            articleUrl = articleList[i][1]
            response = requests.get(articleUrl)
            soup = BeautifulSoup(response.text, 'lxml')
            url = soup.select('ignore_js_op img')
            for imgUrl in url:
                imgFile = imgUrl.get('zoomfile')
                if imgFile == None:
                    continue
                # print(imgFile)
                imgList.append(imgFile)

        if max_num != 0:
            return random.sample(imgList, max_num)

        return imgList 

'''
Test my code to see whether it could work normally.
'''
if __name__ == '__main__':
    beauty = Beauty()
    arr = beauty.getArticle('2021/12/09', 1)
    # print(arr, len(arr))
    imgList = beauty.getImgUrl(arr, 10)
    print(imgList)
    print(len(imgList))

    