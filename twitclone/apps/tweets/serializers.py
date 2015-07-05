from django.forms import widgets
from rest_framework import serializers
from tweets.models import Tweet

class TweetSerializer(serializers.Serializer):
	tid = serializers.IntegerField(read_only=True)
	tweet_user = serializers.CharField(max_length=100)
	tweet_text = serializers.CharField(max_length=140)
	tweet_date = serializers.DateTimeField()

	def create(self, validated_data):
		return Tweet.objects.create(**validated_data)
