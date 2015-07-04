from django.contrib import admin

# Register your models here.
from .models import Tweet
class TweetAdmin(admin.ModelAdmin):
	list_display = ('tweet_text', 'tweet_date')
admin.site.register(Tweet, TweetAdmin)
