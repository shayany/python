from flask import  Flask,render_template
import  feedparser

app=Flask(__name__)

RSS_FEED = {'bbc':"http://feeds.bbci.co.uk/news/world/rss.xml",
            'cnn':"http://rss.cnn.com/rss/edition.rss",
            'fox':'http://feeds.foxnews.com/foxnews/latest'}

@app.route("/<publication>")
@app.route("/")
def get_news(publication='bbc'):
    feed = feedparser.parse(RSS_FEED[publication])
    return  render_template("home.html",articles=feed['entries'])

if __name__=="__main__":
    app.run(port=5000,debug=True)