var app = angular.module("farmSD", ["firebase"]);

app.controller("farmController", function($scope, $firebaseObject) {
	var ref = new Firebase("https://farmsd.firebaseio.com/modules");
  // download the data into a local object
  var syncObject = $firebaseObject(ref);
  // synchronize the object with a three-way data binding
  syncObject.$bindTo($scope, "data");
 // Google Maps Scripts
// When the window has finished loading create our google map below




google.maps.event.addDomListener(window, 'load', init);

function init() {

	var coorRef = new Firebase("hhttps://farmsd.firebaseio.com/coordinates");

	coorRef.on("value", function (snapshot) {
		$scope.moduleCoordinates = snapshot.val();


		var mapOptions = {
        // How zoomed in you want the map to start at (always required)
        zoom: 17,

        // The latitude and longitude to center the map (always required)
        center: new google.maps.LatLng($scope.moduleCoordinates.A.lat, $scope.moduleCoordinates.A.lon), // Hunters

        // Disables the default Google Maps UI components
        disableDefaultUI: true,
        scrollwheel: true,
        draggable: true,

        // How you would like to style the map. 
        // This is where you would paste any style found on Snazzy Maps.
        // styles: [
        // ]
    };

    // Get the HTML DOM element that will contain your map 
    // We are using a div with id="map" seen below in the <body>
    var mapElement = document.getElementById('map');

    // Create the Google Map using out element and options defined above
    var map = new google.maps.Map(mapElement, mapOptions);

    // Custom Map Marker Icon - Customize the map-marker.png file to customize your icon
    var image = 'img/map-marker.png';
    var LatLngA = new google.maps.LatLng($scope.moduleCoordinates.A.lat, $scope.moduleCoordinates.A.lon);
    var LatLngB = new google.maps.LatLng($scope.moduleCoordinates.B.lat, $scope.moduleCoordinates.B.lon);
    var LatLngC = new google.maps.LatLng($scope.moduleCoordinates.C.lat, $scope.moduleCoordinates.C.lon);
    var LatLngD = new google.maps.LatLng($scope.moduleCoordinates.D.lat, $scope.moduleCoordinates.D.lon);
    var LatLngE = new google.maps.LatLng($scope.moduleCoordinates.E.lat, $scope.moduleCoordinates.E.lon);

    var markerA = new google.maps.Marker({
    	position: LatLngA,
    	map: map,
    	icon: image
    });
    var markerB = new google.maps.Marker({
    	position: LatLngB,
    	map: map,
    	icon: image
    }); 
    var markerC = new google.maps.Marker({
    	position: LatLngC,
    	map: map,
    	icon: image
    }); 
    var markerD = new google.maps.Marker({
    	position: LatLngD,
    	map: map,
    	icon: image
    }); 
    var markerE = new google.maps.Marker({
    	position: LatLngE,
    	map: map,
    	icon: image
    }); 
    var tableA = document.getElementById('tableA');//.cloneNode(false);

    var tableB = document.getElementById('tableB');
    var tableC = document.getElementById('tableC');
    var tableD = document.getElementById('tableD');
    var tableE = document.getElementById('tableE');

    var infowindow1 = new google.maps.InfoWindow({
    	content: tableA
    });
    var infowindow2 = new google.maps.InfoWindow({
    	content: tableB
    });
    var infowindow3 = new google.maps.InfoWindow({
    	content: tableC
    });
    var infowindow4 = new google.maps.InfoWindow({
    	content: tableD
    });
    var infowindow5 = new google.maps.InfoWindow({
    	content: tableE
    });
    

    google.maps.event.addListener(markerA, 'click', function() {
    	infowindow1.open(map,markerA);
    });
    google.maps.event.addListener(markerB, 'click', function() {
    	infowindow2.open(map,markerB);
    });
    google.maps.event.addListener(markerC, 'click', function() {
    	infowindow3.open(map,markerC);
    });
    google.maps.event.addListener(markerD, 'click', function() {
    	infowindow4.open(map,markerD);
    });
    google.maps.event.addListener(markerE, 'click', function() {
    	infowindow5.open(map,markerE);
    });
    // Basic options for a simple Google Map
    // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
    // END OF MAPS

    // Anything with firebase goes here

}, function (errorObject) {
	console.log("The read failed: " + errorObject.code);
});

// Charts start here
}

}); // maincontroller end here

app.controller('dataController', ['$scope', function($scope) {

	$scope.items = [
	{ id: 1, module: 'A' },
	{ id: 2, module: 'B' },
	{ id: 3, module: 'C' },
	{ id: 4, module: 'D' },
	{ id: 5, module: 'E' }
	];

	$scope.selectedItem = $scope.items[0];

    // Selector Function
    $scope.getChart = function () {
      switch($scope.selectedItem.id) {
         case 1:
         {
            console.log("You selected one");
        }
        break;
        case 2:
        {
            console.log("You selected two");
        }
        break;
        case 3:
        {
            console.log("You selected three");
        }
        break;
        case 4:
        {
            console.log("You selected four");
        }
        break;
        case 5:
        {
            console.log("You selected five");
        }
        break;
        default:
        {
            console.log("No code selected");
        }
    }

    console.log($scope.selectedItem.id);

};
	google.setOnLoadCallback(drawChart)

  function drawChart() {
     var data = google.visualization.arrayToDataTable([
        ['Module ', 'Sales', 'Expenses'],
        ['2004',  1000,      400],
        ['2005',  1170,      460],
        ['2006',  660,       1120],
        ['2007',  1030,      540]
        ]);

     var options = {
        title: 'Company Performance',
        curveType: 'function',
        legend: { position: 'bottom' }
    };

    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}

google.setOnLoadCallback(drawChart2)

function drawChart2() {
 var data = google.visualization.arrayToDataTable([
    ['Module ', 'Sales', 'Expenses'],
    ['2004',  1000,      400],
    ['2005',  1170,      460],
    ['2006',  660,       1120],
    ['2007',  1030,      540]
    ]);

 var options = {
    title: 'Company Performance',
    curveType: 'function',
    legend: { position: 'bottom' }
};

var chart = new google.visualization.LineChart(document.getElementById('chart_div2'));

chart.draw(data, options);
}




}]);


