var app = angular.module("edit_modules", ['ui.sortable']);

app.config(function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	$httpProvider.defaults.headers.common['Content-Type'] = 'application/json; charset=utf-8';
	$httpProvider.defaults.useXDomain = true;
	$httpProvider.defaults.headers.common['Accept'] = 'application/json, text/javascript';
});

app.controller('myCtrl', function($scope, $http, $q) {

	$scope.form_info = {};
	
	var course_id = document.getElementById("course_id").innerHTML;
	$scope.learner_id = document.getElementById("learner_id").innerHTML;
	var url = "/api/registration_courses/";
	var query_string = url + course_id + "/";

	$scope.query_string = query_string;

	$http.get(query_string).then(successCallback, errorCallback);	
	function successCallback(response){
		$scope.course = response.data;
		$scope.modules = $scope.course.modules;
	};
	function errorCallback(error){
		alert("Error Loading Page!");
	};


	$scope.view_module = function(object, index){
		$scope.selected = object;
		if($scope.selected.topics === "undefined"){
			$scope.selected.topics = "No Topics Added."
		};
		try{
			$scope.selected.assignment_name = unescape($scope.selected.Assignment.split('/').pop());
		}
		catch(err){
			$scope.selected.assignment_name = "No File!";
		};
		try{
			$scope.selected.presentation_name = unescape($scope.selected.Presentation.split('/').pop());
		}
		catch(err){
			$scope.selected.presentation_name = "No File!";
		};
		try{
			$scope.selected.video_name = unescape($scope.selected.video.split('/').pop());
		}
		catch(err){
			$scope.selected.video_name = "No File!";
		};
		try{
			$scope.selected.reference_name = unescape($scope.selected.Refernce.split('/').pop());
		}
		catch(err){
			$scope.selected.reference_name = "No File!";
		};
	};

	$scope.take_quiz = function(object){
		$scope.quiz_name = object.quiz[0].quiz_name;
		$scope.questions = object.quiz[0].questions;
		$scope.selected_question = object.quiz[0].questions[0];
		// console.log($scope.selected_question);
	};

	$scope.select_question = function(question){
		$scope.selected_question = question;
	};

	$scope.submit_quiz = function(){
		for(i=0; i < $scope.questions.length; i++){
			// If the user has selected an option
			if($scope.questions[i].selected !== null){
				var url = "/api/learner_qa/";
				var data= {
					"quiz_question": $scope.questions[i].url,
					"learner": "/api/registration_learners/" + $scope.learner_id + "/",
					"chosen_option": $scope.questions[i].selected.url
				};
				console.log(data);
				$http.post(url, data).then(successCallback, errorCallback);			
				function successCallback(response){
					swal("Good job!", "Answer uploaded!", "success");
				};
				function errorCallback(error){
					console.log(error);
					swal("Oops!", "Something went wrong!", "error");			
				};	
			};
			// If the user has not selected an option then pass in the dummy answer with text "No Option Selected". Make sure to create one and pass it's id
			if($scope.questions[i].selected === null){
				var url = "/api/learner_qa/";
				var data= {
					"quiz_question": $scope.questions[i].url,
					"learner": "/api/registration_learners/" + $scope.learner_id + "/",
					"chosen_option": "/api/registration_answer_options/250/"
				};
				console.log(data);
				$http.post(url, data).then(successCallback, errorCallback);			
				function successCallback(response){
					swal("Good job!", "Answer uploaded!", "success");
				};
				function errorCallback(error){
					console.log(error);
					swal("Oops!", "Something went wrong!", "error");			
				};	
			};
		};
	};
});