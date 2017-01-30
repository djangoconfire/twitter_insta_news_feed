(function() {
  var controllers;

  controllers = angular.module('tweetApp.controllers', []);

  controllers.controller('postListController', function($scope, $interval, Posts, MemberStats, HashtagStats) {
    var checkPosts, fetchPosts;
    $scope.exchange_points = [
      {
        name: 'Start',
        lat: '39.700',
        lon: '-78.653'
      }, {
        name: 'Exchange 1',
        lat: '39.701',
        lon: '-78.651'
      }, {
        name: 'Exchange 2',
        lat: '39.708',
        lon: '-78.567'
      }, {
        name: 'Exchange 3',
        lat: '39.662',
        lon: '-78.507'
      }, {
        name: 'Exchange 4',
        lat: '39.616',
        lon: '-78.490'
      }, {
        name: 'Exchange 5',
        lat: '39.603',
        lon: '-78.463'
      }, {
        name: 'Exchange 6',
        lat: '39.627',
        lon: '-78.389'
      }, {
        name: 'Exchange 7',
        lat: '39.705',
        lon: '-78.329'
      }, {
        name: 'Exchange 8',
        lat: '39.697',
        lon: '-78.249'
      }, {
        name: 'Exchange 9',
        lat: '39.701',
        lon: '-78.188'
      }, {
        name: 'Exchange 10',
        lat: '39.689',
        lon: '-78.118'
      }, {
        name: 'Exchange 11',
        lat: '39.612',
        lon: '-78.006'
      }, {
        name: 'Exchange 12',
        lat: '39.612',
        lon: '-77.937'
      }, {
        name: 'Exchange 13',
        lat: '39.630',
        lon: '-77.861'
      }, {
        name: 'Exchange 14',
        lat: '39.594',
        lon: '-77.821'
      }, {
        name: 'Exchange 15',
        lat: '39.550',
        lon: '-77.800'
      }, {
        name: 'Exchange 16',
        lat: '39.513',
        lon: '-77.756'
      }, {
        name: 'Exchange 17',
        lat: '39.473',
        lon: '-77.656'
      }, {
        name: 'Exchange 18',
        lat: '39.457',
        lon: '-77.603'
      }, {
        name: 'Exchange 19',
        lat: '39.438',
        lon: '-77.527'
      }, {
        name: 'Exchange 20',
        lat: '39.380',
        lon: '-77.478'
      }, {
        name: 'Exchange 21',
        lat: '39.380',
        lon: '-77.474'
      }, {
        name: 'Exchange 22',
        lat: '39.293',
        lon: '-77.432'
      }, {
        name: 'Exchange 23',
        lat: '39.293',
        lon: '-77.357'
      }, {
        name: 'Exchange 24',
        lat: '39.147',
        lon: '-77.293'
      }, {
        name: 'Exchange 25',
        lat: '39.128',
        lon: '-77.237'
      }, {
        name: 'Exchange 26',
        lat: '39.099',
        lon: '-77.204'
      }, {
        name: 'Exchange 27',
        lat: '39.070',
        lon: '-77.169'
      }, {
        name: 'Exchange 28',
        lat: '39.053',
        lon: '-77.105'
      }, {
        name: 'Exchange 29',
        lat: '39.021',
        lon: '-77.094'
      }, {
        name: 'Exchange 30',
        lat: '38.963',
        lon: '-77.092'
      }, {
        name: 'Exchange 31',
        lat: '38.962',
        lon: '-77.107'
      }, {
        name: 'Exchange 32',
        lat: '38.907',
        lon: '-77.112'
      }, {
        name: 'Exchange 33',
        lat: '38.890',
        lon: '-77.103'
      }, {
        name: 'Exchange 34',
        lat: '38.892',
        lon: '-77.087'
      }, {
        name: 'Exchange 35',
        lat: '38.867',
        lon: '-77.046'
      }, {
        name: 'Finish',
        lat: '38.873',
        lon: '-77.002'
      }
    ];
    fetchPosts = function() {
        Posts.getLocation(function(location_posts) {
            return $scope.location_posts = location_posts.reverse();
        });
            return Posts.getRecent(function(posts) {
                $scope.posts = posts.all.reverse();
                $scope.tweets = posts.tweets.reverse();
        return $scope.instas = posts.instas.reverse();

      });
    };
    checkPosts = function() {
        return Posts.getRecent(function(posts) {
        $scope.posts = posts.all.reverse();
        $scope.tweets = posts.tweets.reverse();
        $scope.instas = posts.instas.reverse();
        return $scope.location_posts = posts.location;
      });
    };
    fetchPosts();
    $interval(checkPosts, 30000);
    $scope.mapMovedCallback = function(bounds) {
      console.log('You repositioned the map to:');
      console.log(bounds);
    };
    return $scope.mapZoomedCallback = function(bounds) {
      console.log('You zoomed the map to:');
      console.log(bounds.getCenter().toString());
    };
  });

}).call(this);
