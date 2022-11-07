def scrape(api, word, withHashtags):

    result = []
    
    # Get tweets that contain the hashtag #TypeKeywordHere
    # -is:retweet means I don't want retweets
    # lang:en is asking for the tweets to be in english
    query = '#{w} -is:retweet lang:en'.format(w=word)

    # Search recent tweets with specified fields and return 20 results
    try:
        tweets = api.search_recent_tweets(query=query,
                                        tweet_fields=[
                                            'context_annotations', 'created_at', 'entities'],
                                        user_fields=['username', 'location'], expansions='author_id', max_results=20)
        # Get user list from tweets object
        users = {u["id"]: u for u in tweets.includes['users']}

        for tweet in tweets.data:
            user = users[tweet.author_id]

            # If user wants hashtags -> extract from hashtags entity otherwise skip 
            if(withHashtags):
                hashtags = []
                for o in tweet.entities['hashtags']:
                    hashtags.append(o['tag'])
            
            obj = {
                'message': tweet.text.splitlines() if tweet.text else '',
                'tweet': tweet.created_at,
                'tweetedBy': user.username, 
                'hashtags': hashtags if withHashtags else withHashtags, 
                'location': user.location 
            }
            result.append(obj)
    except:
        return "there was an error with that request..."
        
    return result
