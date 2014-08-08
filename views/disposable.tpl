<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A layout example that shows off a blog page with a list of posts.">
    <title>Whisper from {{sender}}}</title>
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
              <header class="post-header">
                <h2 class="post-title">A whisper from {{sender}}</h2>
              </header>
              <div class="post-description">
                <pre>{{content}}</pre>
                <div class='alert error'>Warning: This message has been deleted. Once you close this window this whisper will be lost forever.</div>
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
