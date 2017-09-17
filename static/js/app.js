$(document).ready(function(){
	console.log("page is loaded");

	var countDownDate = new Date("Nov 1, 2017 11:46:00").getTime();
	var x = setInterval(function() {

	    // Get todays date and time
	    var now = new Date().getTime();
	    
	    // Find the distance between now an the count down date
	    var distance = countDownDate - now;
	    
	    // Time calculations for days, hours, minutes and seconds
	    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
	    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
	    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
	    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
	    
	    // Output the result in an element with id="demo"
	    document.getElementById("tiles").innerHTML = "<div>" + days + "</div><div>" + hours + "</div><div>" + minutes + "</div><div>" + seconds + "</div>"; 
	    
	    // If the count down is over, write some text 
	    if (distance < 0) {
	        clearInterval(x);
	        document.getElementById("tiles").innerHTML = "EXPIRED";
	    }
	}, 1000);


	// for closing nav-bar link after click
	$('.nav-link').on('click',function(e) {
 		$('.navbar-collapse').collapse('hide');
 		
	});

	// for smooth scrolling
	$("a").on('click', function(event) {
    
	    // Make sure this.hash has a value before overriding default behavior
	    if (this.hash !== "") {
	      	// Prevent default anchor click behavior
			event.preventDefault();

			// Store hash
			var hash = this.hash;
			var position = ($(hash).offset().top - 80) + 'px';
			console.log("position",position);

			// Using jQuery's animate() method to add smooth page scroll
			// The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
			$('html, body').animate({
				scrollTop: position
				}, 1000, function(){
				// Add hash (#) to URL when done scrolling (default click behavior)
				window.location.hash = hash;
			});
    	} // End if
	});


	//color change based on user input for contact us form 
	

	//color change based on user input for contact us form



    //var contactNamePattern=/^[a-zA-Z]+$/;

    var msg;

    $('#contact_name').keyup(function () {

        var data = $(this).val();

        console.log(data);

        if (data.length >= 1) {

            $(this).parent('div').removeClass('has-warning').addClass('has-success');

        }

        else {

            $(this).parent('div').removeClass('has-success').addClass('has-warning');



        }

       // document.getElementById("cformName").innerHTML = msg;

    });



    var pattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;

    $('#contact_email').keyup(function (e) {

        var data = $('#contact_email').val().trim();

        console.log(data);

        if (data.match(pattern)) {

            $(this).parent('div').removeClass('has-warning').addClass('has-success');

        }

        else {

            $(this).parent('div').removeClass('has-success').addClass('has-warning');

        }

    });





    var text;

    $('#contact_phone_no').keyup(function (e) {

        var data = $('#contact_phone_no').val().trim();

        console.log(data);

        if ((isNaN(data))) {

            $(this).parent('div').removeClass('has-success').addClass('has-warning');

            text = "Enter number only";

        }

        else {

            $(this).parent('div').removeClass('has-warning').addClass('has-success');



        }

        document.getElementById("cformPhone").innerHTML = text;

    });

    // changing of absolute to fixed nav bar
    $(window).scroll(function() {
	    var height = $(window).scrollTop();

	    if(height  > 90) {
	        console.log("condition true");
	        $('.navbar').removeClass('transparent-navbar').addClass('fixed-navbar fixed-navbar-shadow');
	    }
	    else{
	    	console.log("condition false");
	    	$('.navbar').removeClass('fixed-navbar fixed-navbar-shadow').addClass('transparent-navbar');
	    }
	});

	// window.addEventListener("hashchange", function() { scrollBy(10, -50) })
})



//validation for modal


//var charPattern=/^[a-zA-Z]+$/;
var domainPort = '127.0.0.1:8000';

var text;

$('#apply_name').keyup(function () {

    var data = $(this).val();

    console.log(data);

    if (data.length >= 1) {

        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }

    else {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');



    }

});


var pattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;

$('#apply_email').keyup(function (e) {

    var data = $('#apply_email').val().trim();

    console.log(data);

    if (data.match(pattern)) {

        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }

    else {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');

    }

});



var text;

$('#apply_phone_no').keyup(function (e) {

    var data = $('#apply_phone_no').val().trim();

    console.log(data);



    if ((isNaN(data))) {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');

        text = "Enter number only";

    }

    else {

        $(this).parent('div').removeClass('has-warning').addClass('has-success');



    }

    document.getElementById("phnum").innerHTML = text;

});



//subscription email



var pattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;



$('#sub-email').keyup(function (e) {

    var data = $('#sub-email').val().trim();

    console.log(data);

    if (data.match(pattern)) {

        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }

    else {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');

    }

});


var emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;

var validateEmail = function(data){
    console.log('validate email',data);
    return data.match(emailPattern)? true:false;
}

var subscribe_user = function(){
    var email = $('#subscribe_user_email').val().trim();
    console.log('subscribe user',JSON.stringify({'email':email}));
    if(validateEmail(email)){
        var requestData = {'email':email};
        console.log("valid email");
         $.ajax({
            url: 'http://127.0.0.1:5000/ic/subscribe',
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            dataType:'json',
            crossDomain: true,
            data:JSON.stringify(requestData),
            success: function (data) {
               if(data.notification.code == 200){
                    console.log("subscribe successfull")
               }
               else{
                    console.log("subscribe failed")
               }
            }
        });
    }
    else{
        console.log("INvalid email");
    }
    return false;
}

var applyForCarrer = function(el){
    console.log("apply for carrer",el);
    $('#apply_error').html('');
    var requestData = {},errMsg = '';
    requestData.name = $('#apply_name').val();
    requestData.email = $('#apply_email').val();
    requestData.phone = $('#apply_phone_no').val();
    requestData.role = $('#apply_designation').val();
    console.log('form data',requestData);
    if(!requestData.name || !requestData.email || !requestData.phone || !requestData.role){
        errMsg = 'All fields are required.'
        $('#apply_error').html(errMsg);
    }
    else if(!validateEmail(requestData.email)){
        errMsg = 'Enter valid email adresss.';
         $('#apply_error').html(errMsg);
    }
    else if(isNaN(requestData.phone)){
        errMsg = 'Enter valid phone Number.';
         $('#apply_error').html(errMsg);
    }
    else{
        console.log('api calling');
         $.ajax({
            url: 'http://127.0.0.1:5000/ic/careers',
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            dataType:'json',
            crossDomain: true,
            data:JSON.stringify(requestData),
            success: function (data) {
               if(data.notification.code == 200){
                    console.log("apply successfull")
               }
            },
            error:function(data){
                 if(data.notification.code == 500){
                    console.log("apply failed");
               }
            }
        });
    }
}

var contactUs = function(){
    $('#contact_error').html('');
    var requestData = {},errMsg = '';
    requestData.name = $('#contact_name').val();
    requestData.email = $('#contact_email').val();
    requestData.phone = $('#contact_phone_no').val();
    console.log("contactus",requestData);
    if(!requestData.name || !requestData.email || !requestData.phone ){
        errMsg = 'All fields are required.'
        $('#contact_error').html(errMsg);
    }
    else if(!validateEmail(requestData.email)){
        errMsg = 'Enter valid email adresss.';
         $('#contact_error').html(errMsg);
    }
    else if(isNaN(requestData.phone)){
        errMsg = 'Enter valid phone Number.';
         $('#contact_error').html(errMsg);
    }
    else{
        console.log('api calling');
         $.ajax({
            url: 'http://127.0.0.1:5000/ic/contactus',
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            datatype:'json',
            crossDomain: true,
            data:JSON.stringify(requestData),
            success: function (data) {
               if(data.notification.code == 200){
                    console.log("apply successfull")
               }
            },
            error:function(data){
                 if(data.notification.code == 500){
                    console.log("apply failed");
               }
            }
        });
    }
}

