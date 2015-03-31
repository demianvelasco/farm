var app = angular.module("sampleApp", ["firebase"]);
// a factory to create a re-usable Profile object
// we pass in a username and get back their synchronized data as an object
app.factory("Profile", ["$firebase", function($firebase) {
  return function(username) {
    // create a reference to the user's profile
    var ref = new Firebase("https://farmsd.firebaseio.com/sensors").child(username);
    // return it as a synchronized object
    return $firebase(ref).$asObject();
  }
}]);

app.controller("ProfileCtrl", ["$scope", "Profile",
  function($scope, Profile) {
    // create a three-way binding to our Profile as $scope.profile
    Profile("ground").$bindTo($scope, "profile");
    Profile("temperature").$bindTo($scope, "temperature");
    Profile("moisture").$bindTo($scope, "moisture");
    Profile("airtemp").$bindTo($scope, "airtemp");
    Profile("humidity").$bindTo($scope, "humidity");
    Profile("photosensor").$bindTo($scope, "photosensor");


  }
]);





