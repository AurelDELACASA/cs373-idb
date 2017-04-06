var mainApp = angular.module('mainApp', ['ngRoute', 'smart-table']);

var prefix = "";
if (location.hostname == 'localhost' || location.hostname == '127.0.0.1')
    prefix = "http://localhost:5000"

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
	.when('/participant/:id', {
		templateUrl: '../static/htmls/participant.html',
		controller: 'participantCtrl'
	})
	//Go to tournaments page
	.when('/tournaments', {
		templateUrl: '../static/htmls/tournaments.html',
		controller: 'tournamentsCtrl'
	})
    //Go to tournament page
   	.when('/tournament/:id', {
		templateUrl: '../static/htmls/tournament.html',
		controller: 'tournamentCtrl'
	})
	//Go to characters page
	.when('/characters', {
		templateUrl: '../static/htmls/characters.html',
		controller: 'charactersCtrl'
	})
	//Go to character page
	.when('/character/:id', {
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

mainApp.factory('participantsFactory', function($http) {
  var participantsFactory = {
    async: function() {
      var promise = $http.get(prefix + "/api/participants").then(function (response) {
        return response.data["participants"];
      });
      return promise;
    }
  };
  return participantsFactory;
});

mainApp.controller('participantsCtrl',
  function(participantsFactory, $scope) {
    participantsFactory.async().then(function(data) {
      $scope.participants = data;
      $scope.subset = data;
      $scope.itemsByPage = 10;
      $scope.numPages = 10;
      console.log($scope.numPages);
    });
  });

mainApp.factory('tournamentsFactory', function($http) {
  var tournamentsFactory = {
    async: function() {
      var promise = $http.get(prefix + "/api/tournaments").then(function (response) {
        return response.data["tournaments"];
      });
      return promise;
    }
  };
  return tournamentsFactory;
});

mainApp.controller('tournamentsCtrl',
  function(tournamentsFactory, $scope) {
    tournamentsFactory.async().then(function(data) {
      $scope.tournaments = data;
      $scope.subset = data;
      $scope.itemsByPage = 5;
      $scope.numPages = 10;
      console.log($scope.numPages);
    });
  });

mainApp.controller('tournamentCtrl',
    function ($scope, $routeParams, $http) {
	  	$http.get(prefix + '/api/tournament/' + $routeParams['id'])
		  	.then(function(response) {
                $scope.tournament = response.data["tournament"];
	  	});

});

mainApp.controller('participantCtrl',
    function ($scope, $routeParams, $http) {
        $http.get(prefix + '/api/participant/' + $routeParams['id'])
            .then(function(response) {
                $scope.participant = response.data["participant"];
        });

});


mainApp.factory('charactersFactory', function($http) {
  var charactersFactory = {
    async: function() {
      var promise = $http.get(prefix + "/api/characters").then(function (response) {
        return response.data["characters"];
      });
      return promise;
    }
  };
  return charactersFactory;
});

mainApp.controller('charactersCtrl',
  function(charactersFactory, $scope) {
    charactersFactory.async().then(function(data) {
      $scope.characters = data;
      $scope.subset = data;
      $scope.itemsByPage = 5;
      $scope.numPages = 3;
      console.log($scope.numPages);
    });
  });

mainApp.controller('characterCtrl',
    function ($scope, $routeParams, $http) {
        $http.get(prefix + '/api/character/' + $routeParams['id'])
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
      description: "I'm a 3rd year CS major who enjoys coffee, plants, looking at my denim, and long walks on the beach.",
      responsibilities: 'API Documentation, Tests, AngularJS, Knick Knacks',
      tests: 9,
      issues: 1,
      commits: 0
    },
    {
      name: 'Maurya Avirneni',
      username: 'MauryaAvirneni',
      description: "What's up! I'm Maurya, a junior UTCS student. I'm a fan of full-stack application development, networking and security, and finance. I also enjoy sports and shredding the guitar.",
      responsibilities: 'AngularJS, Bootstrap, AWS',
      tests: 0,
      issues: 17,
      commits: 0
    },
    {
      name: 'Rohit Venugopal',
      username: 'RohitVen',
      description: "Hey, my name is Rohit and I'm a junior here at UT. I love solving Rubik's cubes, longboarding, dancing and computer science! I love Smash and main Ganondorf in Project M. Feel free to ask me for a game!",
      responsibilities: 'Bootstrap, Media',
      tests: 0,
      issues: 1,
      commits: 0
    },
    {
      name: 'Dallas Kelle',
      username: 'DKelle',
      description: "My name is Dallas, and I’m a senior at the University of Texas. My true loves include Computer Science, dogs, and most of all, Melee. I hope this website has helped satisfy your burning desire for Smash stats.",
      responsibilities: 'Bootstrap, AngularJS, Media, AWS',
      tests: 0,
      issues: 6,
      commits: 0
    },
    {
      name: 'Caelan Evans',
      username: 'caelanevans',
      description: "Hi! My name is Caelan and I'm a senior Computer Science student here at UT. I mostly enjoy doing back-end work but I'm excited to get some more experience with front-end tools like AngularJS.",
      responsibilities: 'Models, Flask, AngularJS, AWS',
      tests: 6,
      issues: 9,
      commits: 0
    }
    ];

    $scope.totals = {
        total_commits: 0,
        total_issues: 34,
        total_unittests: 15
    };

    $scope.runTests = function () {
        $http.get('/api/runTests').then(function(data) {
            $scope.tests = data.data
        });
    }
        $http.get('https://api.github.com/repos/lee-benjamin/cs373-idb/stats/contributors')
            .then(function(response) {
                response = response.data
            for(var i = 0; i < response.length; ++i) {
                username = response[i]['author']['login']
                for(var j = 0; j < members.length; ++j) {
                    console.log(members[j].username + " " + username)
                    if(members[j].username === username) {
                        members[j].commits = response[i].total
                        members[j].avatar_url = response[i]['author']['avatar_url']
                        $scope.totals.total_commits += response[i].total
                    }
                }
            }
            $scope.member_stats = members
        });

});
