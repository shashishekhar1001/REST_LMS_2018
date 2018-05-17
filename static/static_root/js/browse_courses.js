var app = angular.module("browse_courses", ['ngRateIt', 'ngFitText']);

app.config(function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	$httpProvider.defaults.headers.common['Content-Type'] = 'application/json; charset=utf-8';
	$httpProvider.defaults.useXDomain = true;
	$httpProvider.defaults.headers.common['Accept'] = 'application/json, text/javascript';
});

app.controller('myCtrl', function($scope, $http, $q) {
	
	$scope.courses = {};
	var url = "/api/paginated_courses/";

	$http.get(url).then(successCallback, errorCallback);	
	function successCallback(response){
		$scope.courses = response.data;
		$scope.next = response.data.next;
	};
	function errorCallback(error){
		swal("Oops!", "Something went wrong!", "error");
	};

	$scope.load_more = function(){
		if($scope.next !== null){
			console.log("Load More");
			$http.get($scope.next).then(successCallback, errorCallback);	
			function successCallback(response){
				$scope.courses.results = $scope.courses.results.concat(response.data.results);	
				$scope.next = response.data.next;													
			};
			function errorCallback(error){
				swal("Oops!", "Something went wrong!", "error");
			};
		}
		else{
			swal("Courses Finished!", "No more courses to show!", "warning");
		};
	};
});
