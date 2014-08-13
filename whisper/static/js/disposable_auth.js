$(document).ready(function() {
  $("#password_one").focus();

  function submit_password(password, message_id) {
    $.post("/disposable/verify", {"password": password, "message_id": message_id}, function(data) {
      if(data.success == "true") {
        $("body").addClass('success_'); 
        $("#auth_form").addClass('animated fadeOutDown');
        $("#success_icon").css('display', 'block').addClass('animated fadeInDown');

        setTimeout(function() {
          window.location.href = "/disposable/" + message_id + "/" + password;
        }, 2000);
      }

      else {
        $("#auth_form").addClass('animated shake');
        $("body").addClass('failure');
        $("#auth_form")[0].reset();
      }
    }, "json");
  }


  $("#password_one").keyup(function() {
    if($(this).val().length == 3) {
      $("#password_two").focus();
    }
  });

  $("#password_two").keyup(function() {
    if($(this).val().length == 3) {
      var password = $("#password_one").val() + "-" + $("#password_two").val();
      var message_id = $("input[name='message_id']").val();

      submit_password(password, message_id);
    }
  })
});