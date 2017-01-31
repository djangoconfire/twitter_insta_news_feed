from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from twython import Twython
from django.views.decorators.csrf import csrf_exempt
import re
import json
import oauth2 as oauth
import json, random, sys, inspect
# Create your views here.

# APP_KEY = 'UWzzBDpA76mQY50HCiOWmTLSm'
# APP_SECRET = 'PPvduM97NnTkDtU8lhxPPgUYObGndugI13OPGeSxauVoE3T3H4'
# ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAOJbXgAAAAAAhtiDPbKZDp0KxUkNcuCUhbDmYSQ%3DXz6kXTSB4hyQ7gshVqqKuRZXDz0DyIVr43SiKiu0q5nXrHFml2'


def get_authenticated_client():
    consumer_key = "UWzzBDpA76mQY50HCiOWmTLSm"
    consumer_secret = "PPvduM97NnTkDtU8lhxPPgUYObGndugI13OPGeSxauVoE3T3H4"
    consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
    request_token_url = "https://api.twitter.com/oauth/request_token"
    client = oauth.Client(consumer)
    return client

def index(request):
    return render(request, 'search.html')

@csrf_exempt  
def search_tweets(request):
    print 'inside predicting tag'
    form_data=request.POST.get('form_data','')
    print form_data
    form_data=json.loads(form_data)
    print form_data
    tweets_list=[]
    for i in range(len(form_data)):
        current_dict=form_data[i]

        if current_dict['name']=='input-search':
            search_list=current_dict['value'].split(',')
            # for debugging
            print search_list
            search_url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + search_list[0]
            client = get_authenticated_client()
            response, data = client.request(search_url)
            tweets = json.loads(data)
            result = random.choice(tweets['statuses'])
            tweets_list.append(result)
    return JsonResponse(tweets_list,safe=False)

@csrf_exempt   
def search_insta(request):
    pass




