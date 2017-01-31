import oauth2 as oauth

def get_authenticated_client():
    consumer_key = "UWzzBDpA76mQY50HCiOWmTLSm"
    consumer_secret = "PPvduM97NnTkDtU8lhxPPgUYObGndugI13OPGeSxauVoE3T3H4"
    consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
    request_token_url = "https://api.twitter.com/oauth/request_token"
    client = oauth.Client(consumer)
    return client