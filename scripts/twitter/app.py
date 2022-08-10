import tweepy
from auth import api_key
from auth import api_key_secret
from auth import access
from auth import access_secret
from tweet import text
# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access,access_secret) 

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

#api.update_status("Test tweet from Tweepy Python")

media = api.media_upload("test.png")
api.update_status(status=text,media_ids=[media.media_id])

