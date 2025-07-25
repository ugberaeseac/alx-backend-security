from django.db import models




class RequestLog(models.Model):
    """
    model to save/log requests
    """
    ip_address = models.CharField(max_length=45)
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.ip_address} - {self.path} - {self.timestamp}'



class BlockedIP(models.Model):
    """ models for blocked ips"""
    ip_address = models.CharField(max_length=45)


    def __str__(self):
        return f'Blocked IP: {self.ip_address}'


class SuspiciousIP(models.Model):
    """ model to save/log suspicious ips """
    ip_address = models.CharField(max_length=45)
    reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ip_address
