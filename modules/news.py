from newsdataapi import NewsDataApiClient
import json


def get_crypto_news(api, to_file=False):
    api = NewsDataApiClient(apikey=api)
    keys = ['Crypto', 'Coin', 'cryptocurrency', 'bitcoin', 'exchange', 'marketcap', 'miners']
    filtered, ks = [], []
    for j in keys:
        response = api.news_api(language='en', q=j)

        for i in response['results']:
            if i['image_url'] is None:
                continue
            if i['title'] in ks:
                continue
            ks.append(i['title'])
            b = {
                'title': i['title'],
                'link': i['link'],
                'image_url': i['image_url'],
                'description': i['description']
            }
            filtered.append(b)

    if to_file:
        f = open(str(to_file) + '.json', 'w')
        f.write(json.dumps(filtered))
        f.close()

    return json.dumps(filtered)
