<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Whisper is an anonymous, encrypted one time email service.">
    <title>Whisper from {{sender}}, anonymously</title>
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
    
    <!--[if lte IE 8]>
      <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/grids-responsive-old-ie-min.css">
    <![endif]-->
    
    <!--[if gt IE 8]><!-->
      <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/grids-responsive-min.css">
    <!--<![endif]-->

    <link rel="stylesheet" href="/static/css/disposable.css">
    <link rel="stylesheet" href="/static/css/animate.css">
    
  </head>
  <body class="auth_page">
    <div id="layout" class="pure-g">
      <div id="auth_container" class="absolute_center">
        <div id="text_logo"><a href="/">Whisper</a></div>
        <div id="success_icon"></div>
        <form id="auth_form" method="post">
          <input id="password_one" name="password_one" minlength="3" maxlength="3">
          <div class="divider"> - </div>
          <input id="password_two" name="password_two" minlength="3" maxlength="3">
          <input type="hidden" name="message_id" value="{{message_id}}">
        </form>
      </div>
    </div>
    <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script src="/static/js/disposable_auth.js"></script>
  </body>
</html>
