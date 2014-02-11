
$(document).ready(function () {

    $(".formDescription").hide();

    $("#id_password").focus(function() {
        $(".formDescription").fadeIn("fast");
    }).blur(function() {
        $(".formDescription").fadeOut("fast");
    });


});