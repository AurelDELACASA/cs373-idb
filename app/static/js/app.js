var mainApp = angular.module('mainApp', ['ngRoute']);

var memberCache = [
{
  name: 'Caelan Evans',
  login: 'caelanevans',
  description: 'My name is Alan. I make data pretty and accessible for their respective audiences. When I\'m not developing, I am drawing and doing photography.',
  responsibilities: 'Full Stack',
  instagram_url: 'https://www.instagram.com/packagedwolf/',
  linkedin_url: 'https://linkedin.com/in/alanmaut',
  pintrest_url: 'https://www.pinterest.com/alanwolfie/',
  tests: 6
},
{
  name: 'Rohit Ven',
  login: 'RohitVen',
  description: 'My name is Alan. I make data pretty and accessible for their respective audiences. When I\'m not developing, I am drawing and doing photography.',
  responsibilities: 'Full Stack',
  instagram_url: 'https://www.instagram.com/packagedwolf/',
  linkedin_url: 'https://linkedin.com/in/alanmaut',
  pintrest_url: 'https://www.pinterest.com/alanwolfie/',
  tests: 6
},
{
  name: 'Ben Lee',
  login: 'lee-benjamin',
  description: 'My name is Alan. I make data pretty and accessible for their respective audiences. When I\'m not developing, I am drawing and doing photography.',
  responsibilities: 'Full Stack',
  instagram_url: 'https://www.instagram.com/packagedwolf/',
  linkedin_url: 'https://linkedin.com/in/alanmaut',
  pintrest_url: 'https://www.pinterest.com/alanwolfie/',
  tests: 6
}
];


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
                $scope.members = memberCache;
	  	});

});

mainApp.controller('participantsCtrl',
    function ($scope, $http) {
        $http.get('http://localhost:5000/api/participants')
            .then(function(response) {
                $scope.participants = response.data["participants"];
        });

});

mainApp.controller('participantCtrl',
    function ($scope, $http) {
        $http.get('http://localhost:5000/api/participant/name1')
            .then(function(response) {
                $scope.participant = response.data["participant"];
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
        GHdata = {};
        $http.get('https://api.github.com/repos/lee-benjamin/cs373-idb/stats/contributors')
            .then(function(data) {

            for(var i = 0; i < data.length; i++) {
                author = data[i]['author']
                GHdata[author.login] = {};
                GHdata[author.login].avatar_url    = author.avatar_url;
                GHdata[author.login].url           = author.html_url;
                GHdata[author.login].contributions = data[i].total;
                GHdata[author.login].issues        = 0;
                stats.commits   += data[i].total;
            }
            $scope.members = memberCache;
            $scope.github = GHdata;
            console.log(memberCache);
        });

});
