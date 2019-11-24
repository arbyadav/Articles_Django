from django.db import models
from time import time


def get_upload_file_name(instance, filename):
    return "Uploaded_Files/%s_%s" % (str(time()).replace('.', '_'), filename)

# Create your models here.


class Article(models.Model):
    article_id = models.IntegerField(unique=True)
    title = models.TextField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('Date Published')
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name)

    def __str__(self):
        return f"{self.title}-{self.article_id}"


class Comment(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('Date Published')
    article = models.ForeignKey('Article', on_delete=models.PROTECT)

    # def __str__(self):
    #     return f"{self.article}"
