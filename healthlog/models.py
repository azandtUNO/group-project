from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class FoodLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

class WorkoutLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField() # in seconds

    def __str__(self):
        return self.name
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
