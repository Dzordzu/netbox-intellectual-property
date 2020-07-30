from django.db import models

class NamedModel(models.Model):
    """ Base for the most models """
    name = models.CharField(max_length=50)

    class Meta:
        ordering = [ 'name' ]
        abstract = True

    def __str__(self):
        return self.name
