from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='pricce',default=0)
    views_count = models.IntegerField(verbose_name='count shows', default=0)

    def __str__(self):
        return self.title
