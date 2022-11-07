# python twitter rest server 

a very simple python rest api that fetches tweets based on a hashtag 

# Key Concepts

* basic rest api 
* use of tweepy (a very good python library to easily access the twitter api) 

# Steps to run this project
1) clone this repository 
2) run `python3 api.py`

# Steps to re-create this project
0.1) curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
0.2) python3 get-pip.py
1) pip3 install Flask
2) pip3 install Flask-RESTful
3) pip3 install Tweepy
4) pip3 install pandas
5) create a file called `api.py` 
6) create twitter developer account -> create app -> get the following keys and save them in an environment file (dotenv)
    - api-key
    - api-secret-key
    - access-token
    - access-token-secret
    - bearer-token
7) initialize flask app with following 
    # `app = Flask(__name__)`
    # `api = Api(app)`
8) create class resources for your endpoints 
    # `class Hello(Resource)`p
    # `class Twitter(Resource)` 
9) in the class resource we can add our get/post/put/delete methods...for this example we will only use get 
10) in the Twitter resource we will create a get method where we extract 2 query params (word & withHashtags)
    - get query parameter by queryParamName = request.args.get('queryParamName')
11) pass query param to our twitter scraper function and return the json value

# example API request 
`http://127.0.0.1:5000/twitter?word=dolphins&withHashtags=true`
