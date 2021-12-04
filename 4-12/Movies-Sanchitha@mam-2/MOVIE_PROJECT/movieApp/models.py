from django.db import models

# Create your models here.


CATEGERY_CHOICE = (
    ('A','ACTION'),
    ('D','DEAMAA'),
    ('C','COMMEDY'),
    ('R','ROMANCE'),
)


LANGUAGE_CHOICES = (
    ('EN','ENGLISH'),
    ('GE','GERMAN'),
    ('EN','ENGLISH'),
    ('HI','HINDHI')
)

STATUS_CHOICES = (
    ('RA','RECENT ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED'),

)

class Movie(models.Model):
    title = models.CharField(max_length=90)
    description = models.TextField(max_length=1000)
    images = models.ImageField(upload_to = 'moviesdata')
    categery = models.CharField(choices=CATEGERY_CHOICE,max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES,max_length=2)
    status = models.CharField(choices=STATUS_CHOICES,max_length=3)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)



