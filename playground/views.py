from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging
import requests

logger = logging.getLogger(__name__)



class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Recived response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('http down')
        return render(request, 'hello.html', {'name': 'Mosh'})
    

class HiView(APIView):     #for test caching
    def get(self, request):
        key = 'httpbin_result'
        cached_data = cache.get(key)

        if cached_data is None:
            response = requests.get('https://httpbin.org/delay/2')
            data = response.json()
            # Add a flag in the cached data
            cached_data = {
                'cached': False,  # Indicate that this data is not cached
                'data': data,
            }
            cache.set(key, cached_data)
        else:
            # Mark the data as cached
            cached_data['cached'] = True

        return render(request, 'hi.html', {'cached_data': cached_data})