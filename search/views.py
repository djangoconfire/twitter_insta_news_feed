from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from twython import Twython
import re
# Create your views here.

APP_KEY = 'UWzzBDpA76mQY50HCiOWmTLSm'
APP_SECRET = 'PPvduM97NnTkDtU8lhxPPgUYObGndugI13OPGeSxauVoE3T3H4'
ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAOJbXgAAAAAAhtiDPbKZDp0KxUkNcuCUhbDmYSQ%3DXz6kXTSB4hyQ7gshVqqKuRZXDz0DyIVr43SiKiu0q5nXrHFml2'


def index(request):
    return render(request, 'search/search.html')

# def searching(request):
#     if request.method == "GET":
#         if 'search_term' in request.GET:
#             query = str(request.GET.get('search_term', ''))
#             try:
#                 pass



def keyword_search(request):
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']
        if query is not None and query != '':
            twitter = Twython()
            twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

            search_results = []
            MAX_ATTEMPTS = 100
            TWEETS = 1000

            for i in range(0,MAX_ATTEMPTS):

                if (TWEETS < len(search_results)):
                    break

                if (0 == i):
                    results = twitter.search(q=query, count=100, result_type='mixed')
                else:
                    results = twitter.search(q=query, include_entities='true', max_id=next_max_id, count=100,  result_type='mixed')

                # raise Exception(results)

                for result in results['statuses']:
                    search_results.append(result)
                try:

                    next_results_url_params = results['search_metadata']['next_results']
                    next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
                except:
                    break

            b=[]
            
            # for tweet in search_results:
            #     source = tweet.get('_source')
            #     a={}
            #     a['lat'] = source.get('location').get('lat')
            #     a['lon'] = source.get('location').get('lon')
            #     a['title'] = re.escape(source.get('title')) 
            #     b.append(a)    

            #search_results = twitter.search(q=query, count=100)
            context = {
                'search_results': search_results,'tweets':b
            }

            return render(request, 'search/search_results.html', context)
        else:
            context = {
                'error': 'You need to enter a search term.',
            }

            return render(request, 'search/search.html', context)


