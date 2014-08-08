$(document).ready(function() {
  _done = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";

  function generate_alert(alert, type) {
    type = type || "alert";

    var id = Math.random().toString(36).substring(3, 9);
    var message = type.charAt(0).toUpperCase() + type.slice(1) + ": " + alert;

    $("#form_container").append("<div id='" + id + "'class=\"alert " + type + " animated fadeInUp\">" + message + "</div>");
    $("#"+id).one(_done, function() {
      setTimeout(function() {
        $("#" + id).addClass("animated fadeOutDown");
        $("#" + id).one(_done, function() {
          $(this).remove();
        }); 
      }, 3000);
    });
  }

  $("#whisper").submit(function(e) {
    e.preventDefault();

    var values = $("#whisper").serializeArray();
    var matrix = {
      "address": "Email address",
      "content": "Whisper content",
      "paranoia": "Paranoia level"
    };
    var fail = false;

    $.each(values, function(i, field) {
      if(field.value == "") {
        $("#whisper").addClass('animated flash');
    
        $("#whisper").one(_done, function() {
          $("#whisper").removeClass('animated flash');
        });

        generate_alert(matrix[field.name] + " is required.", "error");
        fail = true;

        return false;
      }
    });
    
    if(!fail) {
      $.post("/send", $("#whisper").serialize(), function(data) {
        if(data.success == "true") {
          generate_alert("Message sent successfully.", "success");

          $("#background_cover").show();
          $("#success_modal").show().addClass("animated flipInX");
          $("#whisper").addClass('blurred transparent');
        }

        else {
          generate_alert(data.response, "error");
        }
      }, "json")
      .fail(function(jqXHR, textStatus) {
        generate_alert("Message failed to send due to internal server errors. " + textStatus, "error");
      });
    }
  });

  $("#success_modal_clear").click(function() {
    $("#background_cover").hide();
    $("#success_modal").removeClass("animated flipInX").fadeOut(400);
    $("#whisper").removeClass("blurred");
    $("#whisper")[0].reset();
  });
});