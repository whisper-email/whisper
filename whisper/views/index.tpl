<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Whisper is an anonymous, encrypted one time email service.">
    <title>Whisper. Anonymous encrypted email.</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/pure-min.css">
    
    <!--[if lte IE 8]>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/grids-responsive-old-ie-min.css">
    <![endif]-->
    
    <!--[if gt IE 8]><!-->
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/grids-responsive-min.css">
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
        %if sent is not None and sent > 10:
        <h2>{{sent}} whispers sent anonymously.</h2> 
        %end
        <div id="form_container">
          <form id="whisper" method="post">

            <div id="whisper_header" class="pure-g">
              <div class="pure-u-2-5 pure-u-sm-5-24 pure-u-md-4-24">
                <span>Whisper to</span>
              </div>
              <div class="pure-u-3-5 pure-u-sm-14-24 pure-u-md-15-24">
                <input name="address" placeholder="e.snowden@gmail.com">
              </div>
              <div class="pure-u-2-24 pure-u-sm-1-24">
                <span>as</span>
              </div>
              <div class="pure-u-22-24 pure-u-sm-4-24">
                <input name="sender" placeholder="Anonymous">
              </div>
            </div>

            <textarea id="email_content" name="content" rows="8" placeholder="I think we should meet up and talk, I have some information that might interest you."></textarea>

            <select id="paranoia" name="paranoia">
              <option value="1">Plain Text</option>
              <option value="2">Disposable</option>
              <option value="3">Two factor authentication</option>
            </select>

            <div class="pure-g">
              <div class="pure-u-1 pure-u-sm-6-24">
                <div id="security_name">Plain Text</div>
              </div>

              <div class="pure-u-1 pure-u-sm-18-24">
                <div id="security_description">Your message will be sent in plain text over email. It is recommended that if you choose this option you use <a href='http://www.bitcoinnotbombs.com/beginners-guide-to-pgp/'>PGP</a>.</div>
              </div>

              <div class="pure-u-12-24">
                <ul id="security" name="security">
                  <li value="1" class="active low_security">Low</li>
                  <li value="2" class="medium_security">Medium</li>
                  <li value="3" class="high_security">High</li>
                </ul>
              </div>

              <div class="pure-u-12-24">
                <button type="submit" class="pure-button pure-button-primary">send my whisper</button>
              </div>
              
              <div class="pure-u-1">
                <div id="sms_container">
                  <div>
                    Send a secret verification code to:
                    <input id="sms_number" name="number" placeholder="1 888 555 1234">
                  </div>
                </div>
              </div>

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
        <div>
        </div>
      </div>
    </div>
    <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script src="/static/js/index.js"></script>
  </body>
</html>
