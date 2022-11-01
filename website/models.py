from django.db import models
import datetime

class Article(models.Model):
    color = models.CharField('color', max_length=20)
    color_title = models.CharField('Title', max_length=20)
    article = models.CharField('article',max_length=2000)
    add_date = models.DateTimeField('Add date', default=datetime.datetime.now())
    name_prompt = models.CharField('article',max_length=1000, default="")
    poem_prompt = models.CharField('article',max_length=1000, default="")