from django.db import models

class BruteForceAttack(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    country = models.CharField(max_length=3, blank=True, null=True, default="N-N")
    is_success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username+" "+self.ip_address
