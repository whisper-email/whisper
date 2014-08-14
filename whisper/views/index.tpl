<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A layout example that shows off a blog page with a list of posts.">
    <title>whisper. Anonymous encrypted email.</title>
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
    
    <!--[if lte IE 8]>
      <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/grids-responsive-old-ie-min.css">
    <![endif]-->
    
    <!--[if gt IE 8]><!-->
      <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/grids-responsive-min.css">
    <!--<![endif]-->

    <link rel="stylesheet" href="static/css/index.css">
    <link rel="stylesheet" href="static/css/animate.css">
    
  </head>
  <body>
    <div id="layout" class="pure-g">
      <div class="sidebar pure-u-1 pure-u-md-1-4">
        <div class="header">
          <hgroup>
            <h1 class="brand-title">whisper</h1>
            <h2 class="brand-tagline">Anonymous, encrypted email.</h2>
          </hgroup>
        </div>
      </div>

      <div class="content pure-u-1 pure-u-md-3-4">
        <div>
          <div class="posts">
            <div class="post">
              <header class="post-header">
                <h2 class="post-title">Let's talk about Whisper.</h2>
              </header>
              <div class="post-description">
                <p>
                  Well, the way they make shows is, they make one show. That show's called a pilot. Then they show that show to the people who make shows, and on the strength of that one show they decide if they're going to make more shows. Some pilots get picked and become television programs. Some don't, become nothing. She starred in one of the ones that became nothing.
                </p>

                <p>
                  Now that there is the Tec-9, a crappy spray gun from South Miami. This gun is advertised as the most popular gun in American crime. Do you believe that shit? It actually says that in the little book that comes with it: the most popular gun in American crime. Like they're actually proud of that shit. 
                </p>

                <p>
                  Now that we know who you are, I know who I am. I'm not a mistake! It all makes sense! In a comic, you know how you can tell who the arch-villain's going to be? He's the exact opposite of the hero. And most times they're friends, like you and me! I should've known way back when... You know why, David? Because of the kids. They called me Mr Glass.
                </p>
              </div>
            </div>

            <div id="form_container">
              <form id="whisper" method="post">
                
                <div class="whisper_header">
                  <span>Send a whisper to </span>
                  <input name="address" placeholder="e.snowden@gmail.com">
                  <span> from </span>
                  <select name="sender">
                    <option value="Someone">Someone</option>
                    <option value="Anonymous">Anonymous</option>
                    <option value="A friend">A friend</option>
                    <option value="An enemy">An enemy</option>
                  </select>
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
            </div>
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

          <div class="footer">
            <div class="pure-menu pure-menu-horizontal pure-menu-open">
              <ul>
                <li><a href="http://purecss.io/">About</a></li>
                <li><a href="http://twitter.com/yuilibrary/">Twitter</a></li>
                <li><a href="http://github.com/yui/pure/">GitHub</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script src="static/js/index.js"></script>
  </body>
</html>
