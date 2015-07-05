from django.db import models

# Create your models here.
class Tweet(models.Model):
	tweet_user = models.CharField(max_length=100)
	tweet_text = models.CharField(max_length=140)
	tweet_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.tweet_text
	class Meta:
		ordering = ('-tweet_date',)
