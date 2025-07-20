from django.db import models




class RequestLog(models.Model):
    """
    model to save/log requests
    """
    ip_address = models.CharField(max_length=45)
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ip_address} - {self.path} - {self.timestamp}'
