Whisper
-----------------
Anonymous, encrypted email.

Todo:
 - Implement add two-way backend encryption
 - Add ability for original authors to view and optionally delete messages using cookies or sessions.
 - Add optional time expiration
 - Implement docker for painless installation

###Installing Whisper
Whisper is a Python3 application.

####Requirements
 - Python 3.4+
 - Gunicorn
 - Bottle (Included)
 - Requests (pip install requests)

####Example Nginx config
    server {
      listen 80;
      server_name www.whisper.email;
      rewrite ^ http://whisper.email$request_uri? permanent;
    }

    server {
      listen 80;
      server_name whisper.email;
      root /var/www/whisper.email;

      location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      }

      location /static {
        try_files $uri $uri/ =404;
      }

      include php.conf;
    }


###Setting up Whisper
Run 'gunicorn app' from your root Whisper directory to start.

Whisper config will be automatically generated in your root folder if it isn't already present, the config follows this structure:

    {
      "api_key": "",
      "domain": "yourdomain.com",
      "salt": ""
    }

Note that if a salt is not provided then it will automatically be generated.
To acquire an API key (10,000 free emails a month) head here: http://mailgun.com
