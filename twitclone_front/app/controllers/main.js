angular.module('TwitcloneApp')
	.controller('MainCtrl', ['$scope', 'ipsumService', 'Tweets', function($scope, ipsumService, Tweets) {
		$scope.tweets = [];
		Tweets.get({}, function(tweets) {
			$scope.tweets = tweets;
		});
	}]);
