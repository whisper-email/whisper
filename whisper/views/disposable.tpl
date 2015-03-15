<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Whisper is an anonymous, encrypted one time email service.">
    <title>Whisper from {{sender}}, anonymously.</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/pure-min.css">
    
    <!--[if lte IE 8]>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/grids-responsive-old-ie-min.css">
    <![endif]-->
    
    <!--[if gt IE 8]><!-->
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/grids-responsive-min.css">
    <!--<![endif]-->

    <link rel="stylesheet" href="/static/css/disposable.css">
    <link rel="stylesheet" href="/static/css/animate.css">
    
  </head>
  <body>
    <div id="layout" class="pure-g">
      <div class="pure-u-1">
        <div id="text_logo">Whisper</div>
      </div>
      <div id="content" class="disposable_container unread pure-u-1">
        <div class="disposable_title">
          <h1>A whisper from {{sender}}</h1>
        </div>
        <div class="disposable_content unread">{{content}}</div>
        <div class='alert error'>This message has been deleted. Once you close this window this whisper will be lost forever.</div>
      </div>
    </div>
    <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
  </body>
</html>
