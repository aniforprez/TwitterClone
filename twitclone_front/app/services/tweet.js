angular.module('TwitcloneApp')
	.factory('Tweets', ['$resource', function($resource) {
		return $resource('http://localhost:3000/api/tweets/:id', {}, {
			'get': { method: 'GET' }
		})
	}]);
