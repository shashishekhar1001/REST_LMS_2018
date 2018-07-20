var app = angular.module("checkout", []);

app.config(function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	$httpProvider.defaults.headers.common['Content-Type'] = 'application/json; charset=utf-8';
	$httpProvider.defaults.useXDomain = true;
	$httpProvider.defaults.headers.common['Accept'] = 'application/json, text/javascript';
});

app.controller('myCtrl', function($scope, $http, $q) {
    console.log("Checkout.js Loaded");
    var cart = document.getElementById("cart").innerHTML;
    $scope.cart = JSON.parse(cart);
    for(i = 0; i < $scope.cart.length; i++){
        $scope.cart[i].time = 1;
        $scope.cart[i].cost = 10;
    }
    $scope.total_cost = 0;
    for(i = 0; i < $scope.cart.length; i++){
        $scope.total_cost = $scope.total_cost + $scope.cart[i].cost;        
    }
    $("#cart").hide();

    // Start Paypal Section
    paypal.Button.render({
        
        // env: 'sandbox', // sandbox | production
        env: 'production', // sandbox | production

        // PayPal Client IDs - replace with your own
        // Create a PayPal app: https://developer.paypal.com/developer/applications/create
        client: {
            sandbox:    'AZDxjDScFpQtjWTOUtWKbyN_bDt4OgqaF4eYXlewfBP4-8aqX3PiV8e1GWU6liB2CUXlkA59kJXE7M6R',
            production: 'Afz2dSzSuchdJWgK39Qbli8AeeXbwuvLmdcStXN_cY4oXLhxKCI5vWP2YEkh8oRIXYqP9CYjPl1SdXrn'
        },

        // Show the buyer a 'Pay Now' button in the checkout flow
        commit: true,

        // payment() is called when the button is clicked
        payment: function(data, actions) {

            // Make a call to the REST api to create the payment
            return actions.payment.create({
                payment: {
                    transactions: [
                        {
                            amount: { total: $scope.total_cost, currency: 'INR' }
                        }
                    ]
                }
            });
        },

        // onAuthorize() is called when the buyer approves the payment
        onAuthorize: function(data, actions) {

            // Make a call to the REST api to execute the payment
            return actions.payment.execute().then(function() {
                window.alert('Payment Complete!');
            });
        }

    }, '#paypal-button');
    // End Paypal Section
});