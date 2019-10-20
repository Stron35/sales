from bs4 import BeautifulSoup
from random import choice
import requests
import csv
from math import ceil

def price_to_string(name_price, price):
    price_string = [string for string in price if name_price in string.lower()][0].split(': ')[1].split(' р')[0]
    if '\xa0' in price_string:
        price_string = ''.join(price_string.split('\xa0'))
    return price_string

def write_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file,delimiter = ';', lineterminator='\n')
        writer.writerow((data['name'],
                         data['new_price'],
                         data['old_price'],
                         data['image_link'],
                         data['link']))

def get_html(url,useragent=None, proxy=None):
    print('get_html')
    print(useragent, proxy)
    r = requests.get(url, headers = useragent, proxies = proxy)
    return r.text

def get_data(html):
    print('get_data')
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('article')
    for article in articles:
        a = article.find('a')
        try:
            title = a.get('aria-label')
        except:
            title = ''
        print(title)
        title = title.split(', ')
        name = title[0]
        price = [string for string in title if 'цена' in string.lower()]
        try:
            price_new = price_to_string('текущая', price)
        except:
            continue
        try:
            price_old = price_to_string('начальная', price)
        except:
            continue
        try:
            link = a.get('href')
        except:
            link = ''
        try:
        #? непонятно как это работает(весь try)
            # print(type(a.find('img').get('src')))
            image_link = 'http:'+a.find('img').get('src')
            # print()
            # print('Image link')
            # print(image_link)

        except Exception as ex:
            print()
            # template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            # message = template.format(type(ex).__name__, ex.args)
            # print(message)
            # print(image_link)
            # print(type(image_link))
        print(title)
        print('Old price')
        print(price_old)
        print('New price')
        print(price_new)
        print('Image link')
        print(image_link)
        print('Source link')
        print(link,'\n')
        data= {'name':name,
               'new_price':price_new,
               'old_price':price_old,
               'image_link':image_link,
               'link':link}
        write_csv(data)

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    progress = soup.find('progress')
    max = int(progress.get('max'))
    min = int(progress.get('value'))
    print(ceil(max / min))
    return ceil(max / min)

def main():
    url = 'https://www.asos.com/ru/search/?page=1&q=%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0'
    useragents = open('useragent.txt').read().split('\n')
    proxies = open('proxy.txt').read().split('\n')
    base_url = 'https://www.asos.com/ru/search/?page='
    query_set = '&q=%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0'
    for i in range(1):
        proxy = {'http':'http://'+choice(proxies)}
        useragent = {'User-Agent':choice(useragents)}
        if proxy['http']=='http://' or useragent['User-Agent']=='http://':
            proxy = {'http':'http://'+choice(proxies)}
            useragent = {'User-Agent':choice(useragents)}

        try:
            html = get_html(url, useragent, proxy)
        except:
            continue
        total_pages = get_total_pages(html)
        for page in range(1,total_pages):
            print(page)
            gen_url = base_url + str(page) + query_set
            html = get_html(gen_url, useragent, proxy)
            get_data(html)
    # get_data(get_html(url))

if __name__ == '__main__':
    main()


# https://www.asos.com/ru/men/rasprodazha/cat/?cid=8409
