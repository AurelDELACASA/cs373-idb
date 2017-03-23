var mainApp = angular.module('mainApp', ['ngRoute']);

mainApp.config(['$routeProvider', '$locationProvider',
	function($routeProvider, $locationProvider) {
		$routeProvider
	//Go to splash page
	.when('/', {
		templateUrl: '../static/htmls/splash.html',
	})
	//Go to players page
	.when('/participants', {
		templateUrl: '../static/htmls/participants.html',
		controller: 'participantsCtrl'
	})
	//Go to tournaments page
	.when('/tournaments', {
		templateUrl: '../static/htmls/tournaments.html',
		controller: 'tournamentsCtrl'
	})
	//Go to highlights page
	.when('/characters', {
		templateUrl: '../static/htmls/characters.html',
		controller: 'charactersCtrl'
	})
	//Go to about page
	.when('/about', {
		templateUrl: '../static/htmls/about.html',
		controller: 'aboutCtrl'
	})
	.otherwise({redirectTo: '/'});

	//Get rid of # in URL
	if(window.history && window.history.pushState){
		$locationProvider.
		html5Mode({
			enabled: true,
			requireBase: false
		});
	}
}]);


mainApp.controller('tournamentsCtrl',
    function ($scope, $http) {
	  	$http.get('http://localhost:5000/api/tournaments')
		  	.then(function(response) {
		  		$scope.tournaments = response.data["tournaments"];
	  	});

});

mainApp.controller('participantsCtrl',
    function ($scope, $http) {
        $http.get('http://localhost:5000/api/participants')
            .then(function(response) {
                $scope.participants = response.data["participants"];
        });

});

mainApp.controller('charactersCtrl',
    function ($scope, $http) {
        $http.get('http://localhost:5000/api/characters')
            .then(function(response) {
                $scope.characters = response.data["characters"];
        });

});

mainApp.controller('aboutCtrl',
    function ($scope, $http) {
        $http.get('http://localhost:5000/api/tournaments')
            .then(function(response) {
                $scope.tournaments = response.data["tournaments"];
        });

});
