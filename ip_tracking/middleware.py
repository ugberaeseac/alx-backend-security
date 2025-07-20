"""
IP Tracking Middleware

"""

from datetime import datetime
from .models import RequestLog



class IPLoggingMiddleware():
    """
    middleware to log the IP address, timestamp
    and path of every incoming request
    """
    def __init__(self, get_response):
        """ initialize"""
        self.get_response = get_response

    def __call__(self, request):
        ip_address = self.get_ip_address(request)
        path = request.path
        timestamp = datetime.now()

        RequestLog.objects.create(
                ip_address=ip_address,
                timestamp=timestamp,
                path=path)

        response = self.get_response(request)
        return response

    def get_ip_address(self, request):
        """ get the ip address from the request"""
        x_forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_ip:
            ip = x_forwarded_ip.split(',')[0]
            return ip
        ip = request.META.get('REMOTE_ADDR')
        return ip
