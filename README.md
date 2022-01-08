# Twitter-Search-API-V2-Tweet-Classification-OpenAI
In this repo, I included code that utilises the both new twitter API V2 tweepy and OpenAI API to search for tweets online and classify them. This can be used for sentiment analysis, or to filter through tweets for whatever reason.

## YouTube Tutorial Series
This Repo will work best with the youtube video [Twitter Search API V2 Tweet Classification: OpenAI AI API](https://www.youtube.com/watch?v=HpSj25hVPeE)

You will also need to watch these Video Series
[Twitter API V2 API](https://www.youtube.com/watch?v=EXhgOBllQVY&list=PLATQCFQn9lGc1T2aD72wY9rc8N5H4ZoZ3)
[OpenAI API - Getting Started, Starter App](https://www.youtube.com/watch?v=mBVaf3FnVL8&list=PLATQCFQn9lGe3xJmyb6ZRENcHptqNR5gs)

## Using the code

### Step 1
Clone the repo

### Step 2
add your twitter keys in the config.py file

API_KEY = 'add-your-key'
API_KEY_SECRET = 'add-your-key'
BEARER_TOKEN = 'add-your-key'
ACCESS_TOKEN = 'add-your-key'
ACCESS_TOKEN_SECRET = 'add-your-key'
OPENAI_API_KEY = ''

### Replace the tweet training file for your usecase
The tweet classification only works after you have replaced the training file with your own and upload it to OpenAI, get a document reference and replace the document reference in the code.

Files to Complete:
```
tweet-training.jsonl
```

You also need to add the document reference for the training file you upload to OpenAI in this file:
line 7
```sh
openaix.py
```


### Step 4
Install the libraries

```sh
pip install tweepy
```
```sh
pip install flask
```
```sh
pip install openai
```
