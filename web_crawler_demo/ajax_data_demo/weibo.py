from urllib.parse import urlencode
import requests
from pyquery import  PyQuery as pq
from pymongo import MongoClient

#爬取微博
base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) Applewebkit/537.36 (KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

# linux设置：bindIP更改为0.0.0.0  开放端口27017
client = MongoClient('mongodb://43.226.158.95:27017/')
db = client['weibo']
collection = db['weibo']

def save_to_mongo(result):
    if collection.insert_one(result):
        print('Save to Mongo')

if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)


