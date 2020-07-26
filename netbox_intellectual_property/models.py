from django.db import models

class SoftwareProvider(models.Model):
    name = models.CharField(max_length=32)
    full_name = models.CharField(max_length=64)

    class Meta:
        ordering = [ 'name' ]

    def __str__(self):
        return self.name
