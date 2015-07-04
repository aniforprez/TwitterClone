from django.db import models

# Create your models here.
class Tweet(models.Model):
	tweet_text = models.CharField(max_length=140)
	tweet_date = models.DateTimeField('tweet date')
	def __str__(self):
		return self.tweet_text
