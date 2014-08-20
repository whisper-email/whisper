<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Whisper is an anonymous, encrypted one time email service.">
    <title>Whisper. Anonymous encrypted email.</title>
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
    
    <!--[if lte IE 8]>
      <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/grids-responsive-old-ie-min.css">
    <![endif]-->
    
    <!--[if gt IE 8]><!-->
      <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/grids-responsive-min.css">
    <!--<![endif]-->

    <link rel="stylesheet" href="/static/css/index.css">
    <link rel="stylesheet" href="/static/css/animate.css">
    
  </head>
  <body>
    <div id="layout" class="pure-g">
      <div class="pure-u-1">
        <div id="text_logo"><a href="/">Whisper</a></div>
      </div>
      <div id="content" class="pure-u-1">
        %if sent > 1:
        <h2>{{sent}} whispers sent anonymously.</h2> 
        %end
        <div id="form_container">
          <form id="whisper" method="post">

            <div class="whisper_header pure-g">
              <div class="pure-u-2-5 pure-u-sm-6-24">
                <span>Send a whisper to </span>
              </div>
              <div class="pure-u-3-5 pure-u-sm-12-24">
                <input name="address" placeholder="e.snowden@gmail.com">
              </div>
              <div class="pure-u-1 pure-u-sm-6-24">
                <div style="display: inline-block; float: left;"> from </div>
                <div style="display: inline-block; float: right;">
                  <select name="sender">
                    <option value="Someone">Someone</option>
                    <option value="Anonymous">Anonymous</option>
                    <option value="A friend">A friend</option>
                    <option value="An enemy">An enemy</option>
                  </select>
                </div>
              </div>
            </div>

            <textarea id="email_content" name="content" rows="5" placeholder="Meet me under the clocktower at 11 O'Clock."></textarea>

            <select id="paranoia" name="paranoia">
              <option value=""> Paranoia Level </option>
              <option value="1">Plain Text</option>
              <option value="2">Disposable message</option>
              <option value="3">SMS authentication</option>
            </select>
            
            <button type="submit" class="pure-button pure-button-primary">send my whisper</button>
            <div id="sms_container">
              Send a secret verification code to:
              <input id="sms_number" name="number" placeholder="1 888 555 1234">
            </div>
          </form>
          <div id="success_modal" class="absolute_center">
            <div id="success_modal_head">&nbsp;</div>
            <div id="success_modal_body">
              <div class="title">Success!</div>
              <div class="text">Your message has been sent.</div>
              <div id="success_modal_clear" class="pure-button success rounded">send another</div>
            </div>
          </div>
          <div id="background_cover">&nbsp;</div>
        </div>
      </div>
    </div>
    <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script src="/static/js/index.js"></script>
  </body>
</html>
