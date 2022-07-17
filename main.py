from flask import Flask, redirect, url_for, render_template, send_from_directory
from pycoingecko import CoinGeckoAPI
from modules import news, email
from flask_cors import CORS
from flask import request
import datetime
import requests
import random
import string
import redis
import json
import os

# video:
json_file = open('config.json')
config = json.load(json_file)

cg = CoinGeckoAPI()
ds = config['ds']

app = Flask(__name__, template_folder=config['template_folder'])
app.secret_key = config['APP_SECRET_KEY']

CORS(app, resources={r"/*": {"origins": "*"}})

PORT = int(os.environ.get('PORT', 5000))
r = redis.from_url(config['redis-URI'])

sender_mail = config['corporative-email']
password = config['corporative-email-password']


# Settings
@app.route('/', methods=['GET'])
def zero():
    return redirect(url_for('home'), code=302)


@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/api', methods=['GET'])
def api():
    return render_template('api.html')


@app.route('/static/<path:path>', methods=['GET'])
def static_files(path):
    return send_from_directory('static', path)


# APIs
@app.route('/arsen_posts', methods=['GET'])
def arsen_posts():
    # r.set('news', str(news.get_crypto_news(config['cryptonews_api'], False)))
    # print(r.get('news').decode("utf-8"))
    # print(len(json.loads(r.get('news').decode("utf-8"))))
    dick = [
        {
            'title': 'I Am Gay',
            'image_url': 'https://i.ibb.co/1TFXjB5/photo-2022-03-17-12-03-58.jpg',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer facilisis nunc et felis rutrum feugiat. Phasellus lorem ex, tincidunt sit amet diam quis, laoreet rhoncus nulla. Vestibulum tristique id est sed pulvinar. Nam elementum eget tellus eget malesuada. Fusce consectetur, felis et euismod faucibus, turpis lacus imperdiet metus, ac ultricies diam urna id nisi. Proin pharetra viverra cursus. Proin ornare ex erat, a luctus orci consequat eu. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam luctus aliquam lacus, sit amet aliquam neque mollis vel. Quisque eleifend pellentesque pulvinar. Nulla facilisi. Quisque ac lorem nec nisi ornare pulvinar in quis nulla. Quisque ut fringilla dolor.',
            'link': 'https://i.ibb.co/1TFXjB5/photo-2022-03-17-12-03-58.jpg'
        },
        {
            'title': 'I Am Gay',
            'image_url': 'https://i.ibb.co/1TFXjB5/photo-2022-03-17-12-03-58.jpg',
            'description': 'I Am Gay',
            'link': 'https://i.ibb.co/1TFXjB5/photo-2022-03-17-12-03-58.jpg'
        },
        {
            'title': 'I Am Gay',
            'image_url': 'https://i.ibb.co/1TFXjB5/photo-2022-03-17-12-03-58.jpg',
            'description': 'I Am Gay',
            'link': 'https://i.ibb.co/1TFXjB5/photo-2022-03-17-12-03-58.jpg'
        }
    ]
    return json.dumps(dick)


@app.route('/news', methods=['GET'])
def new():
    # r.set('news', str(news.get_crypto_news(config['cryptonews_api'], False)))
    print(r.get('news').decode("utf-8"))
    return r.get('news').decode("utf-8")


@app.route('/current_cap/<coin>', methods=['GET'])
def current_cap(coin):
    if not cg.ping():
        return 'Connection down'
    dat = cg.get_coin_market_chart_by_id(id=coin, vs_currency="usd", days="1")
    return f'{dat["market_caps"][0][0]}=>{dat["market_caps"][0][1]}'


@app.route('/caps_chart/<coin>', methods=['GET'])
def caps_chart(coin):
    if not cg.ping():
        return 'Connection down'
    dat = cg.get_coin_market_chart_by_id(id=coin, vs_currency="usd", days="7")
    x, y = [i[0] for i in dat['market_caps']], [i[1] for i in dat['market_caps']]
    ay = (sum(y) / len(y))
    return '{"xValues":' + str(x) + ',"yValues":' + str(y) + ',"Min":' + str(min(y) - ay / 16) + ',"Max":' + str(
        max(y) + ay / 16) + '}'


@app.route('/price_chart/<coin>', methods=['GET'])
def price_chart(coin):
    if not cg.ping():
        return 'Connection down'
    dat = cg.get_coin_market_chart_by_id(id=coin, vs_currency="usd", days="7")
    x, y = [i[0] for i in dat['market_caps']], [i[1] for i in dat['market_caps']]
    ay = (sum(y) / len(y))
    return '{"xValues":' + str(x) + ',"yValues":' + str(y) + ',"Min":' + str(min(y) - ay / 16) + ',"Max":' + str(
        max(y) + ay / 16) + '}'


@app.route('/table', methods=['GET'])
def table():
    print(r.get('table').decode("utf-8"))
    return r.get('table').decode("utf-8")
    if not cg.ping():
        return 'Connection down'
    dat = cg.get_price(ids=ds, vs_currencies='usd,eur', include_market_cap='true', include_24hr_vol='true',
                       include_24hr_change='true', include_last_updated_at='true')
    refuge = []
    for i in dat:
        dat[i].update({"name": i})
        if None in list(dat[i].values()):
            continue
        refuge.append(dat[i])
    # r.set('table', json.dumps(refuge))
    print(r.get('table').decode("utf-8"))
    return r.get('table').decode("utf-8")


@app.route('/raw_data')
def raw_data():
    url = 'https://rest.coinapi.io/v1/exchanges'
    headers = {'X-CoinAPI-Key': config['X-CoinAPI-Key']}
    response = requests.get(url, headers=headers)
    return str(response.content)


# User
@app.route('/set_user_data', methods=['GET', 'POST', 'PUT'])
def set_user_data():
    if request.method == 'GET':
        if request.args.get('pass') == r.get(request.args.get('email')).decode("utf-8"):
            r.set(request.args.get('email') + "_data", request.args.get('dat'))
            return "Complete"
        return "Incorrect email or password"
    if request.method == 'POST' or request.method == 'PUT':
        if request.form.get('pass') == r.get(request.form.get('email')).decode("utf-8"):
            r.set(request.form.get('email') + "_data", request.form.get('dat'))
            return "Complete"
        return "Incorrect email or password"
    return 'Incorrect request'


@app.route('/get_user_data', methods=['GET', 'POST'])
def get_user_data():
    if request.method == 'GET':
        if request.args.get('pass') == r.get(request.args.get('email')).decode("utf-8"):
            return r.get(request.args.get('email') + "_data").decode("utf-8")
        return 'Incorrect email or password'
    if request.method == 'POST':
        if request.form.get('pass') == r.get(request.form.get('email')).decode("utf-8"):
            return r.get(request.form.get('email') + "_data").decode("utf-8")
        return 'Incorrect email or password'
    return 'Incorrect request'


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        code = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        r.set(request.args.get('email'), code + " " + request.args.get('pass'))
        message = f'''
                Hello, {request.args.get('name')}!
                Your confirmation code is: {code}
                Please, do not tell it nobody and not reply to this email

                ...
                {config['company-name']}
                at: {datetime.datetime.now()}
                '''
        email.send_email(config['corporative-email'], config['corporative-email-password'],
                         request.args.get('email'), 'Confirmation code', message)
    if request.method == 'POST':
        code = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        r.set(request.form.get('email'), code + " " + request.form.get('pass'))
        message = f'''
                Hello, {request.form.get('name')}!
                Your confirmation code is: {code}
                Please, do not tell it nobody and not reply to this email

                ...
                {config['company-name']}
                at: {datetime.datetime.now()}
                '''
        email.send_email(config['corporative-email'], config['corporative-email-password'],
                         request.form.get('email'), 'Confirmation code', message)
    return "Complete"


@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    if request.method == 'GET':
        if r.get(request.args.get('email')).decode("utf-8")[:6] == request.args.get('code'):
            r.set(request.args.get('email'), r.get(request.args.get('email')).decode("utf-8")[7:])
            return "Successful"
        return "Unsuccessful"
    if request.method == 'POST':
        if r.get(request.form.get('email')).decode("utf-8")[:6] == request.form.get('code'):
            r.set(request.form.get('email'), r.get(request.form.get('email')).decode("utf-8")[7:])
            return "Successful"
        return "Unsuccessful"
    return 'Incorrect request'


@app.route('/subscribe', methods=['GET', 'POST', 'PATCH'])
def subscribe():
    if request.method == 'GET':
        dat = r.get('subscribers').decode("utf-8") + ',' + request.args.get('email')
        print(request.args.get('email'))
        r.set('subscribers', dat)
        return "Successful"
    if request.method == 'POST' or request.method == 'PATCH':
        dat = r.get('subscribers').decode("utf-8") + ',' + request.form.get('email')
        print(request.form.get('email'))
        r.set('subscribers', dat)
        return "Successful"
    return 'Incorrect request'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
