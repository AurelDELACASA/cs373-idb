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

/*
mainApp.controller('tournamentsCtrl', ['$scope',
    function ($scope) {

  var dict1 = {
    name: "Tourney1",
    date: "6/5/09",
    location: "UT Austin",
    num_entrants: "1",
    imageURL: "/path1"
  };

  var dict2 = {
    name: "Tourney2",
    date: "6/5/10",
    location: "UT Austin",
    num_entrants: "0",
    imageURL: "/path2"
  };

  $scope.tournaments = [dict1, dict2];


}]);
*/