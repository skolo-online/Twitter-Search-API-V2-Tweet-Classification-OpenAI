import os
import openai
import config
openai.api_key = config.OPENAI_API_KEY

#Refer to YouTube Video
class_file = "replace-this-file-id"



def uploadClassificationDocument():
    filename = 'tweet-training.jsonl'
    response = openai.File.create(file=open(filename), purpose="classifications")
    return response


def classifyTweet(query):
    response = openai.Classification.create(
            file=class_file,
            query=query,
            search_model="ada",
            model="curie",
            max_examples=3)

    return response['label']


















###
