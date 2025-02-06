from django.db import models

# Create your models here.
Sessions= [
    ('swimming', 'Swimming'),
    ('biking', 'biking'),
    ('racing', 'Racing'),
    ('meeting', 'Meeting'),
    ]
allergies = [
    ('Dairy', 'Dairy'),
    ('Peanuts', 'Peanuts'),
    ('air', 'air'),
    ]

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(default="test@gmail.com")
    number = models.IntegerField(default=9999999999)
    sessions = models.CharField(choices=Sessions, null = True, blank=True,max_length=50)
    allergies = models.CharField(choices=allergies,max_length=50)

