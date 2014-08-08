<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A layout example that shows off a blog page with a list of posts.">
    <title>Your whisper has been destroyed.</title>
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
    
    <!--[if lte IE 8]>
      <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/grids-responsive-old-ie-min.css">
    <![endif]-->
    
    <!--[if gt IE 8]><!-->
      <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/grids-responsive-min.css">
    <!--<![endif]-->

    <link rel="stylesheet" href="/static/css/site.css">
    
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
          <!-- A wrapper for all the blog posts -->
          <div class="posts">
            <!-- A single blog post -->
            <div class="post">
              <div class="disposed_header">This message does not exist or has been destroyed.</div>
              <div class="post-description">
                <div id="faq">
                  <h2 class="faq_header">Frequently Asked Questions</h2>
                  <div class="faq_content">
                    <h3>What is whisper? Why am I here?</h3>
                    <p>Whisper is an anonymous, and optionally encrypted courier service. You are here because someone sent you a disposable message link.</p>
                    <h3>What happened to my message?</h3>
                    <p>All whispers are immediately destroyed once viewed. If you are seeing this page, you or possibly someone else has already read this whisper.</p>
                    <h3>How do I know I can trust this service?</h3>
                    <p>Whisper is an <a href="http://github.com/whisper-email/whisper">open source project</a>, anyone can audit the source as they see fit.</p>
                    <h3>How do I send whispers of my own?</h3>
                    <p><a href="/">Send a whisper</a></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
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
    <script src="/static/js/site.js"></script>
  </body>
</html>
