"""
IP Tracking Middleware

"""

import requests
from datetime import datetime
from .models import RequestLog, BlockedIP
from django.core.cache import cache
from django_ip_geolocation.utils import get_geoip_data
from django.http import HttpResponseForbidden
from functools import wraps



def get_ip_address(request):
    """ helper function to get ip address from request"""
    x_forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_ip:
        ip = x_forwarded_ip.split(',')[0]
        return ip
    ip = request.META.get('REMOTE_ADDR')
    return ip



class IPLoggingMiddleware():
    """
    middleware to log the IP address, timestamp
    and path of every incoming request
    """
    def __init__(self, get_response):
        """ initialize"""
        self.get_response = get_response

    def __call__(self, request):
        ip_address = get_ip_address(request)
        url = f'https://ipinfo.io/{ip_address}/json'
        key = f'geo_ip:{ip_address}'

        geo_data = cache.get(key)
        if not geo_data:
            try:
                response = requests.get(url, timeout=3)
                if response.status = 200:
                    geo_info = response.json()
                    cache.set(key, geo_info, 3600 * 24)
            except Exception as err:
                geo_info = {}

        path = request.path
        timestamp = datetime.now()
        country = geo_info.get('country', '')
        city = geo_info.get('city', '')


        RequestLog.objects.create(
                ip_address=ip_address,
                timestamp=timestamp,
                path=path,
                country=country,
                city=city)

        response = self.get_response(request)
        return response



class IPBlockingMiddleware():
    """
    block ip based on block list
    """
    def __init__(self, get_response):
        """initialize"""
        self.get_response = get_response

    def __call__(self, request):
        ip_address = get_ip_address(request)
        
        #blocked_ip = BlockedIP.objects.filter(ip_address=ip_address)
        #if blocked_ip:
        #    return HttpResponseForbidden('Access is forbidden from this IP address')
        if BlockedIP.objects.filter(ip_address=ip_address).exists():
            return HttpResponseForbidden('Access is forbidden from this IP address')
        response = self.get_response(request)
        return response




