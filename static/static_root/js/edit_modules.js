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
	var url = "/api/registration_courses/";
	var query_string = url + course_id + "/";

	$scope.query_string = query_string;

	$http.get(query_string).then(successCallback, errorCallback);	
	function successCallback(response){
		$scope.course = response.data;
		$scope.modules = $scope.course.modules;
		$scope.sortableOptions = {
			stop: function(e, ui) {
				$scope.update_order(); 
			},
		};
	};
	function errorCallback(error){
		alert("Error Loading Page!");
	};

	$scope.update_order = function(){
		for(var i = 0; i < $scope.modules.length; i++){
			$scope.modules[i].order = i + 1;			
			var data = {
				"order": $scope.modules[i].order
			};
			var url = $scope.modules[i].url;
			$http.patch(url, data).then(successCallback, errorCallback);
			function successCallback(response){
			};
			function errorCallback(error){
			};		
		}		
	};

	$scope.delete_module = function(object, index){
		swal({
			title: "Are you sure?",
			text: "Once Deleted, you will not be able to recover!",
			icon: "warning",
			buttons: true,
			dangerMode: true,
		  })
		  .then((willDelete) => {
			if (willDelete) {
				$http.delete(object.url).then(successCallback, errorCallback);	
				function successCallback(response){
					$scope.modules.splice(index, 1);
					$scope.update_order();
					swal("Deleted Successfully.", {
						icon: "success",
					});
				};
				function errorCallback(error){
					swal("Deleting Cancelled!");					
				};
			} else {
			  swal("Deleting Cancelled!");
			}
		  });			
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
	};

	$scope.edit_module = function(object, index){
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
		// POPULATE FORM DATA
		$scope.form_info = $scope.selected;
	};


	//Change Module Name Part
	$scope.change_module_name = function(){
		var data = {
			"name":$scope.form_info.name
		};
		var url = $scope.selected.url;
		$http.patch(url, data).then(successCallback, errorCallback);
		function successCallback(response){
			swal("Name Changed!", "Module Name Updated Successfully!", "success");
		};
		function errorCallback(error){
			swal("Oops!", "Something went wrong!", "error");
		};
	}


	//Change Topic Name Part	
	$scope.change_topic = function(){
		var data = {
			"topics":$scope.form_info.topics
		};
		var url = $scope.selected.url;
		$http.patch(url, data).then(successCallback, errorCallback);
		function successCallback(response){
			swal("Topic Changed!", "Topics Updated Successfully!", "success");
		};
		function errorCallback(error){
			swal("Oops!", "Something went wrong!", "error");
		};
	};

	//Video Upload Part	
	$scope.vdo_upload = function(){
		var file_selected = false;		
		var element = document.getElementById("vdo");
		if (element.files[0] === undefined){
			swal("No File Chosen!", "Please select a file to be uploaded!", "error");
		}
		else{
			file_selected = true;
		};
		if (file_selected === true){
		    $scope.show_vdo_progrsess_bar = true;			
			var url = $scope.selected.url;
			var fd = new FormData();
			var canceller = $q.defer();
			$scope.vdo_cancel = function(){
				swal({
					title: "Are you sure?",
					text: "Once aborted, you will not be able to resume!",
					icon: "warning",
					buttons: true,
					dangerMode: true,
				  })
				  .then((willDelete) => {
					if (willDelete) {
					  swal("Upload Cancelled!");
					  canceller.resolve();
					} else {
					  swal("Resuming file upload.", {
						icon: "success",
					});
					}
				  });			
			};
			fd.append('video', element.files[0]);
			$http.patch(url, fd, {
				transformRequest: angular.identity,
				headers: {'Content-Type': undefined},
				uploadEventHandlers: {
					progress: function (e) {
							  if (e.lengthComputable) {
								$scope.vdoprogressBar = Math.floor((e.loaded / e.total) * 95);
							  }
					}
				},
				timeout: canceller.promise
			}).then(successCallback, errorCallback);
			function successCallback(response){
				if (response.status === 200){
					$scope.selected.video = response.data.video;
					$scope.selected.video_name = $scope.selected.video.split('/').pop();
					$scope.selected.video_name = unescape($scope.selected.video_name);
					$scope.vdoprogressBar = $scope.vdoprogressBar + 5;
					$scope.show_vdo_progrsess_bar = false;
					swal("Good job!", "Your file is uploaded!", "success");
				}
			};
			function errorCallback(error){
				if (error.status === -1){
					swal("Aborted!", "File Uploaded Was Aborted!", "error");									
				}
				else{
					swal("Oops!", "Something went wrong....!", "error");									
				}
				$scope.show_vdo_progrsess_bar = false;
			};
		};
	};

	//Assignment Upload Part
	$scope.assignment_upload = function(){
		var file_selected = false;		
		var element = document.getElementById("ass");
		if (element.files[0] === undefined){
			swal("No File Chosen!", "Please select a file to be uploaded!", "error");
		}
		else{
			file_selected = true;
		};
		if (file_selected === true){
		    $scope.show_ass_progrsess_bar = true;			
			var url = $scope.selected.url;
			var fd = new FormData();
			var canceller = $q.defer();
			$scope.ass_cancel = function(){
				swal({
					title: "Are you sure?",
					text: "Once aborted, you will not be able to resume!",
					icon: "warning",
					buttons: true,
					dangerMode: true,
				  })
				  .then((willDelete) => {
					if (willDelete) {
					  swal("Resuming file upload.", {
						icon: "success",
					  });
					} else {
					  swal("Upload Cancelled!");
					  canceller.resolve();
					}
				  });			
			};
			fd.append('Assignment', element.files[0]);
			$http.patch(url, fd, {
				transformRequest: angular.identity,
				headers: {'Content-Type': undefined},
				uploadEventHandlers: {
					progress: function (e) {
							  if (e.lengthComputable) {
								$scope.assprogressBar = Math.floor((e.loaded / e.total) * 95);
							  }
					}
				},
				timeout: canceller.promise
			}).then(successCallback, errorCallback);
			function successCallback(response){
				if (response.status === 200){
					$scope.selected.Assignment = response.data.Assignment;
					$scope.selected.assignment_name = $scope.selected.Assignment.split('/').pop();
					$scope.selected.assignment_name = unescape($scope.selected.assignment_name);
					$scope.assprogressBar = $scope.assprogressBar + 5;
					$scope.show_ass_progrsess_bar = false;
					swal("Good job!", "Your file is uploaded!", "success");
				}
			};
			function errorCallback(error){
				if (error.status === -1){
					swal("Aborted!", "File Uploaded Was Aborted!", "error");									
				}
				else{
					swal("Oops!", "Something went wrong....!", "error");									
				}
				$scope.show_ass_progrsess_bar = false;
			};
		};
	};


	//Presentation Upload Part
	$scope.presentation_upload = function(){
		var file_selected = false;		
		var element = document.getElementById("pres");
		if (element.files[0] === undefined){
			swal("No File Chosen!", "Please select a file to be uploaded!", "error");
		}
		else{
			file_selected = true;
		};
		if (file_selected === true){
		    $scope.show_pres_progrsess_bar = true;			
			var url = $scope.selected.url;
			var fd = new FormData();
			var canceller = $q.defer();
			$scope.pres_cancel = function(){
				swal({
					title: "Are you sure?",
					text: "Once aborted, you will not be able to resume!",
					icon: "warning",
					buttons: true,
					dangerMode: true,
				  })
				  .then((willDelete) => {
					if (willDelete) {
					  swal("Resuming file upload.", {
						icon: "success",
					  });
					} else {
					  swal("Upload Cancelled!");
					  canceller.resolve();
					}
				  });			
			};
			fd.append('Presentation', element.files[0]);
			$http.patch(url, fd, {
				transformRequest: angular.identity,
				headers: {'Content-Type': undefined},
				uploadEventHandlers: {
					progress: function (e) {
							  if (e.lengthComputable) {
								$scope.presprogressBar = Math.floor((e.loaded / e.total) * 95);
							  }
					}
				},
				timeout: canceller.promise
			}).then(successCallback, errorCallback);
			function successCallback(response){
				if (response.status === 200){
					$scope.selected.Presentation = response.data.Presentation;
					$scope.selected.presentation_name = $scope.selected.Presentation.split('/').pop();
					$scope.selected.presentation_name = unescape($scope.selected.presentation_name);
					$scope.presprogressBar = $scope.presprogressBar + 5;
					$scope.show_pres_progrsess_bar = false;
					swal("Good job!", "Your file is uploaded!", "success");
				}
			};
			function errorCallback(error){
				if (error.status === -1){
					swal("Aborted!", "File Uploaded Was Aborted!", "error");									
				}
				else{
					swal("Oops!", "Something went wrong....!", "error");									
				}
				$scope.show_pres_progrsess_bar = false;
			};
		};
	};


	// Unpopulate form
	$scope.empty_form = function(){
		console.log("Empty Form");	
		$('#add_form')[0].reset();
	};


	// New Module Add
	$scope.add_module = function(){
		$scope.vdo_element = document.getElementById("new_vdo");
		$scope.pres_element = document.getElementById("new_pres");
		$scope.ass_element = document.getElementById("new_ass");

		$scope.fd = new FormData();	
		$scope.show_addmodule_progrsess_bar = true;
		var canceller = $q.defer();	

		if ($scope.vdo_element.files[0] === undefined){
		}
		else{
			$scope.fd.append('video', $scope.vdo_element.files[0]);	
		};

		if ($scope.ass_element.files[0] === undefined){
		}
		else{
			$scope.fd.append('Assignment', $scope.ass_element.files[0]);	
		};

		if ($scope.pres_element.files[0] === undefined){
		}
		else{
			$scope.fd.append('Presentation', $scope.pres_element.files[0]);	
		};

		$scope.fd.append('name', $scope.new_module_name);
		$scope.fd.append("topics", $scope.new_module_topics);
		$scope.fd.append("part_of", $scope.query_string);
		$scope.fd.append("order", $scope.modules.length + 1);

		var url = "/api/registration_courses_modules/"

		$scope.add_cancel = function(){
			swal({
				title: "Are you sure?",
				text: "Once aborted, you will not be able to resume!",
				icon: "warning",
				buttons: true,
				dangerMode: true,
			  })
			  .then((willDelete) => {
				if (willDelete) {
				  swal("Upload Cancelled!");
				  canceller.resolve();
				} else {
				  swal("Resuming Module upload.", {
					icon: "success",
				});
				}
			  });			
		};

		$http.post(url, $scope.fd, {
			transformRequest: angular.identity,
			headers: {'Content-Type': undefined},
			uploadEventHandlers: {
				progress: function (e) {
						  if (e.lengthComputable) {
							$scope.show_add_progrsess_bar = true;
							$scope.addmodule_progressBar = Math.floor((e.loaded / e.total) * 95);
						  }
				}
			},
			timeout: canceller.promise
		}).then(successCallback, errorCallback);

		function successCallback(response){
			if (response.status === 201){
				swal("Good job!", "New module uploaded!", "success");
				$scope.new_module = response.data;				
				$scope.modules.push($scope.new_module);			
				$scope.addmodule_progressBar = $scope.addmodule_progressBar + 5;	
				$scope.show_add_progrsess_bar = false;
			};
		};
		function errorCallback(error){
			if (error.status === -1){
				swal("Aborted!", "Module Uploaded Was Aborted!", "error");									
			}
			else{
				swal("Oops!", "Something went wrong!", "error");
			};
			$scope.show_add_progrsess_bar = false;			
		};
	};
});