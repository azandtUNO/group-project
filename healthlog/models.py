from django.db import models

# Create your models here.
class FoodLog(models.Model):
    user
    name
    description
    time
    calories

class WorkoutLog(models.Model):
    user
    name
    description
    time
    duration