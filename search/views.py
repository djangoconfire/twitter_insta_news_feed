from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from twython import Twython
from django.views.decorators.csrf import csrf_exempt
import re
import json
import json, random, sys, inspect
from util import *
from instagram.client import InstagramAPI
import os

import requests
from pandas.io.json import json_normalize
import pandas as pd
import datetime
from key import *

api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID, 
                   client_secret=INSTAGRAM_CLIENT_SECRET, 
                   client_ips=client_ip,
                   access_token=INSTAGRAM_ACCESS_TOKEN)

 
count=100


def index(request):
    return render(request, 'search.html')

@csrf_exempt  
def search_tweets(request):
    print 'inside predicting twitter tag'
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
            count=0
            while count<10:
                response, data = client.request(search_url)
                tweets = json.loads(data)
                result = random.choice(tweets['statuses'])
                tweets_list.append(result)
                count = count+1
    return JsonResponse(tweets_list,safe=False)

 
@csrf_exempt   
def search_insta(request):
    print 'inside predicting instagram tag'
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
            print search_list[0]

            base_url = "https://api.instagram.com/v1"
            url = '{0}/tags/{1}/media/recent?client_id={2}&count=100'.format(
            base_url, search_list[0], INSTAGRAM_CLIENT_ID)
            print url
            r = requests.get(url)
            j = r.json()  
            results = []
            if 'data' in j: 
                data = j['data']
                df_instance = json_normalize(data)
                results.append(df_instance)
            
            print results    
    return JsonResponse(results,safe=False)




