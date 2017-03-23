var mainApp = angular.module('mainApp', ['ngRoute']);

mainApp.config(['$routeProvider', '$locationProvider',
	function($routeProvider, $locationProvider) {
		$routeProvider
	//Go to splash page
	.when('/', {
		templateUrl: '../static/htmls/splash.html',
	})
	//Go to participants page
	.when('/participants', {
		templateUrl: '../static/htmls/participants.html',
		controller: 'participantsCtrl'
	})
    //Go to particpant page
	.when('/participant/:participantName', {
		templateUrl: '../static/htmls/participant.html',
		controller: 'participantCtrl'
	})
	//Go to tournaments page
	.when('/tournaments', {
		templateUrl: '../static/htmls/tournaments.html',
		controller: 'tournamentsCtrl'
	})
    //Go to tournament page
   	.when('/tournament/:tournamentName', {
		templateUrl: '../static/htmls/tournament.html',
		controller: 'tournamentCtrl'
	})
	//Go to characters page
	.when('/characters', {
		templateUrl: '../static/htmls/characters.html',
		controller: 'charactersCtrl'
	})
	//Go to character page
	.when('/character/:characterName', {
		templateUrl: '../static/htmls/character.html',
		controller: 'characterCtrl'
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
	  	$http.get('http://localhost/api/tournaments')
		  	.then(function(response) {
		  		$scope.tournaments = response.data["tournaments"];
	  	});

});

mainApp.controller('tournamentCtrl',
    function ($scope, $http) {
	  	$http.get('http://localhost/api/tournament/name1')
		  	.then(function(response) {
		  		$scope.tournament = response.data["tournament"];
	  	});

});

mainApp.controller('participantsCtrl',
    function ($scope, $http) {
        $http.get('http://localhost/api/participants')
            .then(function(response) {
                $scope.participants = response.data["participants"];
        });

});

mainApp.controller('participantCtrl',
    function ($scope, $http) {
        $http.get('http://localhost/api/participant/name1')
            .then(function(response) {
                $scope.participant = response.data["participant"];
        });

});

mainApp.controller('charactersCtrl',
    function ($scope, $http) {
        $http.get('http://localhost/api/characters')
            .then(function(response) {
                $scope.characters = response.data["characters"];
        });

});

mainApp.controller('characterCtrl',
    function ($scope, $http) {
        $http.get('http://localhost/api/character/name1')
            .then(function(response) {
                $scope.character = response.data["character"];
        });

});


mainApp.controller('aboutCtrl',
    function ($scope, $http) {
    var members = [
    {
      name: 'Ben Lee',
      username: 'lee-benjamin',
      description: 'Ben description goes here',
      responsibilities: 'Full Stack',
      tests: 3,
      issues: 0,
      commits: 0
    },
    {
      name: 'Maurya Avimeni',
      username: 'MauryaAvimeni',
      description: 'Maurya description goes here',
      responsibilities: 'Full Stack',
      tests: 0,
      issues: 0,
      commits: 0
    },
    {
      name: 'Rohit Ven',
      username: 'RohitVen',
      description: 'Rohit description goes here',
      responsibilities: 'Full Stack',
      tests: 0,
      issues: 0,
      commits: 0
    },
    {
      name: 'Dallas Kelle',
      username: 'DKelle',
      description: 'Dallas description goes here',
      responsibilities: 'Full Stack',
      tests: 0,
      issues: 0,
      commits: 0
    },
    {
      name: 'Caelan Evans',
      username: 'caelanevans',
      description: 'Caelan description goes here',
      responsibilities: 'Full Stack',
      tests: 6,
      issues: 0,
      commits: 0
    }
    ];

    var total_commits = 0;
        $http.get('https://api.github.com/repos/lee-benjamin/cs373-idb/stats/contributors')
            .then(function(response) {
                response = response.data
            for(var i = 0; i < response.length; ++i) {
                total_commits += response[i].total;
                username = response[i]['author']['login']
                for(var j = 0; j < members.length; ++j) {
                    console.log(members[j].username + " " + username)
                    if(members[j].username === username) {
                        members[j].commits = response[i].total
                        members[j].avatar_url = response[i]['author']['avatar_url']
                    }
                }
            }
            $scope.member_stats = members
        });

});
