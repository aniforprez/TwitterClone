angular.module('TwitcloneApp', ['ngMaterial', 'ngResource', 'ngCookies', 'ipsum'])
	.run(function run($http, $cookies ){
	    // For CSRF token compatibility with Django
	    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
	});
