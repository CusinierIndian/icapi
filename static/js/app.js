

$(document).ready(function () {

    console.log("page is loaded");

    var countDownDate = new Date("Nov 1, 2017 11:46:00").getTime();

    var x = setInterval(function () {



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

    $('.nav-link').on('click', function (e) {

        $('.navbar-collapse').collapse('hide');



    });



    // for smooth scrolling

    $("a").on('click', function (event) {



        // Make sure this.hash has a value before overriding default behavior

        if (this.hash !== "") {

            // Prevent default anchor click behavior

            event.preventDefault();



            // Store hash

            var hash = this.hash;

            var position = ($(hash).offset().top - 80) + 'px';

            console.log("position", position);



            // Using jQuery's animate() method to add smooth page scroll

            // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area

            $('html, body').animate({

                scrollTop: position

            }, 1000, function () {

                // Add hash (#) to URL when done scrolling (default click behavior)

                window.location.hash = hash;

            });

        } // End if

    });



    $('.service-card').hover(function () {

        $(this).find('.service-card-text').css('display', 'block');

    }, function () {

        $(this).find('.service-card-text').css('display', 'none');

    })

    //color change based on user input for contact us form





    //color change based on user input for contact us form







    var contactNamePattern = /^[a-zA-Z][a-zA-Z ]+$/;
    var msg;
    $('#contact_name').keyup(function () {



        var data = $(this).val();



        console.log(data);



        if (data.match(contactNamePattern)) {

            if(data.length>1){

            $(this).parent('div').removeClass('has-warning').addClass('has-success');
        }


        }

        else if (data == "") {

            $(this).parent('div').removeClass('has-success').addClass('has-warning');

            msg = "Name field cannot be empty";

        }

        





        else {



            $(this).parent('div').removeClass('has-success').addClass('has-warning');

            msg = "Enter characters only";







        }





        document.getElementById("cformName").innerHTML = msg;



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

    $(window).scroll(function () {

        var height = $(window).scrollTop();



        if (height > 90) {

            console.log("condition true");

            $('.navbar').removeClass('transparent-navbar').addClass('fixed-navbar fixed-navbar-shadow');

        }

        else {

            console.log("condition false");

            $('.navbar').removeClass('fixed-navbar fixed-navbar-shadow').addClass('transparent-navbar');

        }

    });



    // window.addEventListener("hashchange", function() { scrollBy(10, -50) })

})







//validation for modal







var domainPort = '127.0.0.1:8000';

var charPattern = /^[a-zA-Z]+$/;

var text;



$('#apply_name').keyup(function () {

    var data = $(this).val();
    console.log(data);
    if (data.match(charPattern)) {
        $(this).parent('div').removeClass('has-warning').addClass('has-success');
    }

    else if (data == "") {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');

        text = "Name field cannot be empty!!!!";

    }

    else {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');

        text = "Enter characters only";
    }
    document.getElementById("apply_nm").innerHTML = text;
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






//Service house-hold model validation


var serviceNamePattern = /^([a-zA-Z]){2,30}$/;
var msg;
$('#service_name').keyup(function () {

    var data = $(this).val();



    console.log(data);



    if (data.match(serviceNamePattern)) {

        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }

    else if (data == "") {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');

        msg = "Name field cannot be empty";

    }

    else {



        $(this).parent('div').removeClass('has-success').addClass('has-warning');

        msg = "Enter characters only";

    }

    document.getElementById("service_nm").innerHTML = msg;



});







var pattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;



$('#service_email').keyup(function (e) {



    var data = $('#service_email').val().trim();



    console.log(data);



    if (data.match(pattern)) {



        $(this).parent('div').removeClass('has-warning').addClass('has-success');



    }



    else {



        $(this).parent('div').removeClass('has-success').addClass('has-warning');



    }



});





var text;

$('#service_phone_no').keyup(function (e) {



    var data = $('#service_phone_no').val().trim();



    console.log(data);



    if ((isNaN(data))) {



        $(this).parent('div').removeClass('has-success').addClass('has-warning');



        text = "Enter number only";



    }



    else {



        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }



    document.getElementById("service_phone").innerHTML = text;



});


var text;

$('#service_pincode').keyup(function (e) {



    var data = $('#service_pincode').val().trim();



    console.log(data);



    if ((isNaN(data))) {



        $(this).parent('div').removeClass('has-success').addClass('has-warning');



        text = "Enter number only";



    }



    else {



        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }



    document.getElementById("service_pin").innerHTML = text;



});
var text;

$('#service_alternate_phone_no').keyup(function (e) {

    var data = $('#service_alternate_phone_no').val().trim();
    console.log(data);

    if ((isNaN(data))) {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');
        text = "Enter number only";
    }

    else {
        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }
    document.getElementById("service_alternate_phone").innerHTML = text;
});

var msg;
$('#service_address').keyup(function (e) {
    var data = $(this).val();
    console.log(data);
    if (data == "") {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');
         msg = "Address Field cannot be Empty";
    }
    else
    {
        $(this).parent('div').removeClass('has-warning').addClass('has-success');
    }
    
       document.getElementById("service_ad").innerHTML = msg;
    
});



//Service ocassion model validation
var serviceNamePattern = /^([a-zA-Z]){2,30}$/;
var msg;
$('#service_ocassion_name').keyup(function () {

    var data = $(this).val();



    console.log(data);



    if (data.match(serviceNamePattern)) {

        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }

    else if (data == "") {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');

        msg = "Name field cannot be empty";

    }

    else {



        $(this).parent('div').removeClass('has-success').addClass('has-warning');

        msg = "Enter characters only";

    }

    document.getElementById("service_ocassion_nm").innerHTML = msg;



});







var pattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;



$('#service_ocassion_email').keyup(function (e) {



    var data = $('#service_ocassion_email').val().trim();



    console.log(data);



    if (data.match(pattern)) {



        $(this).parent('div').removeClass('has-warning').addClass('has-success');



    }



    else {



        $(this).parent('div').removeClass('has-success').addClass('has-warning');



    }



});





var text;

$('#service_ocassion_phone_no').keyup(function (e) {



    var data = $('#service_ocassion_phone_no').val().trim();



    console.log(data);



    if ((isNaN(data))) {



        $(this).parent('div').removeClass('has-success').addClass('has-warning');



        text = "Enter number only";



    }



    else {



        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }



    document.getElementById("service_ocassion_phone").innerHTML = text;



});


var text;

$('#service_ocassion_pincode').keyup(function (e) {



    var data = $('#service_ocassion_pincode').val().trim();



    console.log(data);



    if ((isNaN(data))) {



        $(this).parent('div').removeClass('has-success').addClass('has-warning');



        text = "Enter number only";



    }



    else {



        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }



    document.getElementById("service_ocassion_pin").innerHTML = text;



});
var text;

$('#service_ocassion_alternate_phone_no').keyup(function (e) {

    var data = $('#service_ocassion_alternate_phone_no').val().trim();
    console.log(data);

    if ((isNaN(data))) {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');
        text = "Enter number only";
    }

    else {
        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }
    document.getElementById("service_ocassion_alternate_phone").innerHTML = text;
});





var msg;
$('#service_ocassion_address').keyup(function (e) {
    var data = $(this).val();
    console.log(data);
    if (data == "") {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');
         msg = "Address Field cannot be Empty";
    }
    else
    {
        $(this).parent('div').removeClass('has-warning').addClass('has-success');
    }
    
       document.getElementById("service_ocassion_ad").innerHTML = msg;
    
});

//----------------

var emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
var validateEmail = function (data) {

    console.log('validate email', data);

    return data.match(emailPattern) ? true : false;

}



/*validation for feedback */
var feedbackNamePattern = /^([a-zA-Z]){2,30}$/;
var msg;
$('#feedback_name').keyup(function () {
    var data = $(this).val();
    console.log(data);
    if (data.match(feedbackNamePattern)) {

        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }

    else if (data == "") {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');

        msg = "Name field cannot be empty";

    }

    else {
        $(this).parent('div').removeClass('has-success').addClass('has-warning');
        msg = "Enter characters only";
    }

    document.getElementById("name").innerHTML = msg;
});


var pattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
$('#feedback_email').keyup(function (e) {
    var data = $('#feedback_email').val().trim();
    console.log(data);
    if (data.match(pattern)) {
        $(this).parent('div').removeClass('has-warning').addClass('has-success');
    }
else {
        $(this).parent('div').removeClass('has-success').addClass('has-warning');
    }
});


var text;
$('#feedback_phone_no').keyup(function (e) {
    var data = $('#feedback_phone_no').val().trim();
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
var feedbackCookNamePattern = /^([a-zA-Z]){2,30}$/;
var msg;
$('#feedback_cook_name').keyup(function () {
    var data = $(this).val();
    console.log(data);
    if (data.match(feedbackCookNamePattern)) {

        $(this).parent('div').removeClass('has-warning').addClass('has-success');

    }

    else if (data == "") {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');

        msg = "Name field cannot be empty";

    }

    else {
        $(this).parent('div').removeClass('has-success').addClass('has-warning');
        msg = "Enter characters only";
    }

    document.getElementById("cook_nm").innerHTML = msg;
});

var msg;
$('#feedback_comment').keyup(function () {
    var data = $(this).val();
    console.log(data);
    if (data == "") {

        $(this).parent('div').removeClass('has-success').addClass('has-warning');
         msg = "Comment field cannot be empty!";
    }
    else
    {
        $(this).parent('div').removeClass('has-warning').addClass('has-success');
    }
    
       document.getElementById("feedback_cmnt").innerHTML = msg;
    
});






var subscribe_user = function () {

    var email = $('#subscribe_user_email').val().trim();

    console.log('subscribe user', JSON.stringify({ 'email': email }));

    if (validateEmail(email)) {

        var requestData = { 'email': email };

        console.log("valid email");

        $.ajax({

            url: 'http://127.0.0.1:5000/ic/subscribe',

            type: 'POST',

            contentType: "application/json; charset=utf-8",

            dataType: 'json',

            crossDomain: true,

            data: JSON.stringify(requestData),

            success: function (data) {

                if (data.notification.code == 200 || data.notification.code == 'ic_500') {

                    console.log("subscribe successfull")

                    $('#subscription-modal-success').modal('show');

                }

                else {

                    console.log("subscribe failed")

                    $('#error-modal').modal('show');

                }

                $('#subscribe_user_email').val('');

            }

        });

    }

    else {

        console.log("Invalid email");

    }

    return false;

}

/*feedback*/
var customerFeedback = function (el) {

   

    $('#feedback_error').html('');

    var requestData = {}, errMsg = '';

    requestData.customerName = $('#feedback_name').val();

    requestData.customerEmail = $('#feedback_email').val();

    requestData.customerPhone = $('#feedback_phone_no').val();

    requestData.feedback = $('#feedback_comment').val();
    requestData.cookName = $('#feedback_cook_name').val();

    console.log('form data', requestData);

    if (!requestData.customerName && !requestData.customerPhone) {

        errMsg = 'Name and Phone number are required.'

        $('#feedback_error').html(errMsg);

    }

    else if (isNaN(requestData.customerPhone) || requestData.customerPhone.length != 10) {

        errMsg = 'Enter valid phone Number.';

        $('#feedback_error').html(errMsg);

    }

    else if (requestData.customerEmail && !validateEmail(requestData.customerEmail)) {

        errMsg = 'Enter valid email.';

        $('#feedback_error').html(errMsg);

    }
    

    else {

        console.log('api calling');

        $.ajax({

            url: 'http://127.0.0.1:5000/ic/feedback',

            type: 'POST',

            contentType: "application/json; charset=utf-8",

            dataType: 'json',

            crossDomain: true,

            data: JSON.stringify(requestData),

            success: function (data) {

                $('#feedback-modal').modal('hide');

                if (data.notification.code == 200) {

                    $('#feedBackSuccess-modal').modal('show');

                }

                else {

                    $('#error-modal').modal('show');

                }

                    $('#feedback_name').val();
                    $('#feedback_email').val();
                    $('#feedback_phone_no').val();
                    $('#feedback_cook_name').val();
                    $('#feedback_comment').val();
            },

            error: function (data) {

                if (data.notification.code == 500) {

                    console.log("submission  failed");

                    $('#error-modal').modal('show');

                }

            }

        });

    }

}





var applyForCarrer = function (el) {

    console.log("apply for carrer", el);

    $('#apply_error').html('');

    var requestData = {}, errMsg = '';

    requestData.name = $('#apply_name').val();

    requestData.email = $('#apply_email').val();

    requestData.phone = $('#apply_phone_no').val();

    requestData.role = $('#apply_designation').val();

    console.log('form data', requestData);

    if (!requestData.name && !requestData.phone) {

        errMsg = 'Name and Phone number are required.'

        $('#apply_error').html(errMsg);

    }

    else if (isNaN(requestData.phone) || requestData.phone.length != 10) {

        errMsg = 'Enter valid phone Number.';

        $('#apply_error').html(errMsg);

    }

    else if (requestData.email && !validateEmail(requestData.email)) {

        errMsg = 'Enter valid email.';

        $('#apply_error').html(errMsg);

    }

    else {

        console.log('api calling');

        $.ajax({

            url: 'http://127.0.0.1:5000/ic/careers',

            type: 'POST',

            contentType: "application/json; charset=utf-8",

            dataType: 'json',

            crossDomain: true,

            data: JSON.stringify(requestData),

            success: function (data) {

                $('#apply-modal').modal('hide');

                if (data.notification.code == 200) {

                    $('#carrer-modal').modal('show');

                }

                else {

                    $('#error-modal').modal('show');

                }

                $('#apply_name').val('');

                $('#apply_email').val('');

                $('#apply_phone_no').val('');

            },

            error: function (data) {

                if (data.notification.code == 500) {

                    console.log("apply failed");

                    $('#error-modal').modal('show');

                }

            }

        });

    }

}



var contactUs = function () {

    $('#contact_error').html('');

    var requestData = {}, errMsg = '';

    requestData.name = $('#contact_name').val();

    requestData.email = $('#contact_email').val();

    requestData.phone = $('#contact_phone_no').val();

    console.log("contactus", requestData);

    //console.log(!requestData.name);





    if (!requestData.name && !requestData.email && !requestData.phone) {

        errMsg = 'All fields are required.'

        $('#contact_error').html(errMsg);

    }



    else if (!validateEmail(requestData.email)) {

        errMsg = 'Enter valid email adresss.';

        $('#contact_error').html(errMsg);

    }

    else if (isNaN(requestData.phone) || requestData.phone.length != 10) {

        errMsg = 'Enter valid phone Number.';

        $('#contact_error').html(errMsg);

    }

    else {

        console.log('api calling');

        $.ajax({

            url: 'http://127.0.0.1:5000/ic/contactus',

            type: 'POST',

            contentType: "application/json; charset=utf-8",

            datatype: 'json',

            crossDomain: true,

            data: JSON.stringify(requestData),

            success: function (data) {

                if (data.notification.code == 200) {

                    console.log("apply successfull")
                    $('#carrer-modal').modal('show');

                }

                else {

                    $('#error-modal').modal('show');

                }

                $('#contact_name').val('');
                $('#contact_email').val('');
                $('#contact_phone_no').val('');

            }

        });

    }

}

var applyForService = function (el) {
    var xyz;
    $('button').click(function (el){

    console.log("apply for service", el);

    $('#service_error').html('');

    var requestData = {}, errMsg = '';

    requestData.bookingfor=$(this).attr('id') 
    requestData.customerName = $('#service_name').val();
    requestData.customerEmail = $('#service_email').val();
    requestData.customerPhone = $('#service_phone_no').val();
    requestData.pincode = $('#service_pincode').val();
    requestData.customerLocation = $('#service_location').val();
    requestData.city = $('#service_city').val();
    requestData.state = $('#service_state').val();
    requestData.address = $('#service_address').val();
    requestData.landmark = $('#service_landmark').val();
    requestData.alternatePhoneNo = $('#service_alternate_phone_no').val();
    requestData.cookPreference= $('#cook_preferences').val();
    requestData.numberOfMembers = $('#no_of_people').val();
    console.log("form data", requestData);

    if (!requestData.customerName && !requestData.customerEmail && !requestData.customerPhone && !requestData.numberOfMembers && !requestData.pincode && !requestData.address) {

        errMsg = 'All fields are required.';

        $('#service_error').html(errMsg);

    }

    else if (isNaN(requestData.customerPhone) || requestData.customerPhone.length != 10) {

        errMsg = 'Enter valid phone Number.';

        $('#service_error').html(errMsg);

    }

    else if (isNaN(requestData.pincode) || requestData.pincode.length != 6) {

        errMsg = 'Enter valid pincode';

        $('#service_error').html(errMsg);

    }

    else if (requestData.address == "") {
        errMsg = 'Enter Address';

        $('#service_error').html(errMsg);

    }

    else if (!validateEmail(requestData.customerEmail)) {

        errMsg = 'Enter valid Email Id.';

        $('#service_error').html(errMsg);

    }

    else if (requestData.numberOfMembers < 1) {

        errMsg = 'Enter valid number of people';

        $('#service_error').html(errMsg);

    }



    else {

        $.ajax({

            url: 'http://127.0.0.1:5000/ic/cookbooking',

            type: 'POST',

            contentType: "application/json; charset=utf-8",

            datatype: 'json',

            crossDomain: true,

            data: JSON.stringify(requestData),

            success: function (data) {

                $('#service-household-modal').modal('hide');

                if (data.notification.code == 200) {

                    console.log("apply successfull")

                    $('#carrer-modal').modal('show');

                }

                else {

                    $('#error-modal').modal('show');

                }

                $('#service_name').val('');
                $('#service_email').val('');
                $('#service_phone_no').val('');
                $('#service_location').val('');
                $('#cook_preferences').val('');
                $('#no_of_people').val('');
                $('#service_address').val('');
                $('#service_landmark').val('');
                $('#service_pincode').val('');
                $('#service_alternate_phone_no').val('');
            }

        });

    }

 });
}

var applyForOccasionalService = function (el) {

    var xyz;
    $('button').click(function (el){

//console.log(xyz);

    
  

    //console.log("apply for service", el);
   
    
    $('#service_error').html('');

    var requestData = {}, errMsg = '';
    requestData.bookingfor=$(this).attr('id') 
    
    requestData.customerName = $('#service_ocassion_name').val();
    requestData.customerEmail = $('#service_ocassion_email').val();
    requestData.customerPhone = $('#service_ocassion_phone_no').val();
    requestData.pincode = $('#service_ocassion_pincode').val();
    requestData.customerLocation = $('#service_ocassion_location').val();
    requestData.city = $('#service_ocassion_city').val();
    requestData.state = $('#service_ocassion_state').val();
    requestData.address = $('#service_ocassion_address').val();
    requestData.landmark = $('#service_ocassion_landmark').val();
    requestData.alternatePhoneNo = $('#service_ocassion_alternate_phone_no').val();
    requestData.cookPreference = $('#service_ocassion_cook_preferences').val();
    requestData.numberOfMembers = $('#service_ocassion_no_of_people').val();
    console.log("form data", requestData);

    if (!requestData.customerName && !requestData.customerEmail && !requestData.customerPhone && !requestData.numberOfMembers && !requestData.pincode && !requestData.address) {

        errMsg = 'All fields are required.';

        $('#service_error').html(errMsg);

    }

    else if (isNaN(requestData.customerPhone) || requestData.customerPhone.length != 10) {

        errMsg = 'Enter valid phone Number.';

        $('#service_error').html(errMsg);

    }

    else if (isNaN(requestData.pincode) || requestData.pincode.length != 6) {

        errMsg = 'Enter valid pincode';

        $('#service_error').html(errMsg);

    }

    else if (requestData.address == "") {
        errMsg = 'Enter Address';

        $('#service_error').html(errMsg);

    }

    else if (!validateEmail(requestData.customerEmail)) {

        errMsg = 'Enter valid Email Id.';

        $('#service_error').html(errMsg);

    }

    else if (requestData.numberOfMembers < 1) {

        errMsg = 'Enter valid number of people';

        $('#service_error').html(errMsg);

    }



    else {

        $.ajax({

            url: 'http://127.0.0.1:5000/ic/cookbooking',

            type: 'POST',

            contentType: "application/json; charset=utf-8",

            datatype: 'json',

            crossDomain: true,

            data: JSON.stringify(requestData),

            success: function (data) {

                $('#service-occasion-modal').modal('hide');

                if (data.notification.code == 200) {

                    console.log("apply successfull")

                    $('#carrer-modal').modal('show');

                }

                else {

                    $('#error-modal').modal('show');

                }

                $('#service_ocassion_name').val('');
                $('#service_ocassion_email').val('');
                $('#service_ocassion_pin').val('');
                $('#service_ocassion_phone_no').val('') 
                $('#service_ocassion_address').val('');
                $('#service_ocassion_landmark').val('');
                $('#service_ocassion_pincode').val('');
                $('#service_ocassion_alternate_phone').val('');
                $('#service_ocassion_no_of_people').val('');
            }

        });

    }
    });

}



