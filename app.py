from flask import Flask, render_template, url_for, redirect, request
import config
import search


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)



@app.route('/', methods=["GET", "POST"])
def index():

    query = 'Project Management lang:en -is:retweet'

    if request.method == 'POST':
        query = '{} lang:en -is:retweet'.format(request.form['query'])

    max_results = 10
    tweets = search.returnSearchTweetList(query, max_results)

    return render_template('index.html', **locals())


@app.route('/retweet/<string:tweetId>/', methods=["GET", "POST"])
def reweet(tweetId):
    search.retweet(tweetId)

    return redirect(url_for('index'))






@app.route('/classify', methods=["GET", "POST"])
def classify():

    query = 'Polokwane lang:en -is:retweet'

    if request.method == 'POST':
        query = '{} lang:en -is:retweet'.format(request.form['query'])


    max_results = 20

    tweets = search.retrieveClasiffyTweets(query, max_results)

    positiveTweets = []
    negativeTweets = []
    neutralTweets = []

    for tweet in tweets:
        if tweet['classx'] == 'Positive':
            positiveTweets.append(tweet)
        if tweet['classx'] == 'Negative':
            positiveTweets.append(tweet)
        if tweet['classx'] == 'Neutral':
            positiveTweets.append(tweet)

    return render_template('class.html', **locals())















if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
