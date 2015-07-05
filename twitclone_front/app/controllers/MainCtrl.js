angular.module('TwitcloneApp')
	.controller('MainCtrl', ['$scope', 'ipsumService', function($scope, ipsumService) {
		$scope.tweets = [];
		for(var i = 0; i < 20; i++) {
			$scope.tweets.push({
				tweet_user: ipsumService.randomFirst() + " " + ipsumService.randomLast(),
				tweet_text: ipsumService.sentences(2),
				tweet_date: new Date()
			});
		}
	}]);
