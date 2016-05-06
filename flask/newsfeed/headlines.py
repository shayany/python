from flask import Flask, render_template, request
import feedparser
import urllib
import urllib2
import json

app = Flask(__name__)

RSS_FEED = {'bbc': "http://feeds.bbci.co.uk/news/world/rss.xml",
            'cnn': "http://rss.cnn.com/rss/edition.rss",
            'fox': 'http://feeds.foxnews.com/foxnews/latest'}

DEFAULTS = {'publication': 'bbc',
            'city': 'London,UK',
            'currency_from': 'GBP',
            'currency_to': 'USD'}

CURRENCY_URL = "https://openexchangerates.org/api/latest.json?app_id=b5a06bb9d70249e99bcdc3b111426dd1"


@app.route("/", methods=['GET', 'POST'])
def home():
    publication = request.args.get("publication")

    if not publication:
        publication = DEFAULTS['publication']
    articles = get_news(publication)

    city = request.args.get('city')
    if not city:
        city = DEFAULTS['city']

    weather = get_weather(city)


    currency_from = request.args.get('currency_from')
    if not currency_from:
        currency_from = DEFAULTS['currency_from']

    currency_to = request.args.get('currency_to')
    if not currency_to:
        currency_to = DEFAULTS['currency_to']
    rate, currencies= get_rates(currency_from, currency_to)
    return render_template("home.html", articles=articles,
                           weather=weather,
                           currency_from=currency_from,
                           currency_to=currency_to,
                           rate=rate,currencies=sorted(currencies))


def get_news(query):
    if not query or query.lower() not in RSS_FEED:
        publication = DEFAULTS['publication']
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEED[publication])
    return feed['entries']


def get_weather(query):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=92daf5ff7cfc997f587cf999c44040fe"
    query = urllib.quote(query)  # Handling whitespaces
    url = api_url.format(query)  # Insert name of the city into URL
    data = urllib2.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {"description": parsed["weather"][0]["description"],
                   "temperature": parsed["main"]["temp"],
                   "city": parsed["name"],
                   "country": parsed['sys']['country']}
    return weather


def get_rates(frm, to):
    all_currency = urllib2.urlopen(CURRENCY_URL).read()
    parsed = json.loads(all_currency).get('rates')
    frm_rate = parsed.get(frm.upper())
    to_rate = parsed.get(to.upper())
    return (to_rate / frm_rate, parsed.keys())


if __name__ == "__main__":
    app.run(port=5000, debug=True)
