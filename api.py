# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import tweepy
import os
from dotenv import load_dotenv
from functions import scrape

load_dotenv()

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.

class Hello(Resource):

    def get(self):
        return "Welcome to the api"


class Twitter(Resource):
    def get(self):
        # get query params from request
        word = request.args.get('word')
        withHashtags = request.args.get('withHashtags')
        print("request param: ", withHashtags)
        if withHashtags == 'true':
            flag = True
        else:
            flag = False

        if (word):
            return jsonify(scrape(twitter_client, word, flag))
        else:
            return jsonify({
                "message": "Missing query parameter!",
                "field": "word"
            })


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Twitter, '/twitter')

# driver function
if __name__ == '__main__':

    # authenticate with twitter api and verify
    api_key = os.environ.get("api-key")
    api_secret_key = os.environ.get("api-secret-key")
    access_token = os.environ.get("access-token")
    access_token_secret = os.environ.get("access-token-secret")
    bearer_token = os.environ.get("bearer-token")

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    twitter_client = tweepy.Client(bearer_token)

    try:
        twitter_client._get_authenticating_user_id
        print("everything is working!")
    except:
        print("there was an issue during authentication")

    app.run(debug=True)
