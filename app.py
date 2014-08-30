from bottle import Bottle, TEMPLATE_PATH, static_file, request, template, run
from bottle_sqlite import SQLitePlugin

from whisper import _database
from whisper import _utils
from whisper import _init

import json

# Extend the bottle class to initialize the DB and config
class WhisperApp(Bottle):

  def __init__(self, catchall=True, autojson=True):
    self.app_config = _init.init_config() # Necessary due to naming conflicts in the Bottle class
    self.database = _database
    self.utils = _utils

    _init.init_db()
    super().__init__()

app = WhisperApp()
app.install(SQLitePlugin(dbfile="whisper/db/whisper.db"))
TEMPLATE_PATH.insert(0, 'whisper/views')

# Todo: add cookies.
@app.route('/', template="index")
def index(db):
  stats = app.database.get_stats(db)
  if stats is None:
    return dict(sent=None, opened=None)
  else:
    sent, opened = stats
    return dict(sent=sent, opened=opened)

@app.route('/faq', template="faq")
def faq():
  return dict()

# Todo: Allow the original sender to view and optionally destroy message using cookies.
@app.route('/disposable/<message_id>')
@app.route('/disposable/<message_id>/<auth>')
def view_whisper(message_id, db, auth=None):
  message = app.database.get_disposable(message_id, db)

  if message is None:
    return template("disposable_expired")

  sender, content, password = message

  if password:
    if auth is not None and auth == password:
      app.database.delete_disposable(message_id, db)
      app.database.update_stats("opened", db)
      return template("disposable", sender=sender, content=content)  

    return template("disposable_auth", sender=sender, message_id=message_id)
  
  app.database.delete_disposable(message_id, db)
  app.database.update_stats("opened", db)
  return template("disposable", sender=sender, content=content)

@app.post('/disposable/verify')
def verify_whisper(db):
  query = request.forms.get('password')
  message_id = request.forms.get('message_id')

  message = app.database.get_disposable(message_id, db)

  if message is None:
    return json.JSONEncoder().encode({
      "success": "false"
    })

  sender, content, password = message
  
  result = "true" if password == query else "false"

  return json.JSONEncoder().encode({
    "success": result
  })

@app.post('/send')
def send_whisper(db):
  address = request.forms.get('address')
  sender = request.forms.get('sender')
  content = request.forms.get('content')
  paranoia = request.forms.get('paranoia')
  password = request.forms.get('password')
  number = request.forms.get('number')

  try:
    sender = sender or "Anonymous"
    message_id = app.utils.gen_id()
    formatted_content = content
    
    url = "http://%s/disposable/%s" % (app.app_config.get("domain"), message_id)

    if int(paranoia) is 1:
      password = None
      url = None
      app.database.update_stats("opened", db)

    # Paranoia == Disposable Message
    if int(paranoia) is 2:
      password = None
      formatted_content = ("Someone has sent you a whisper anonymously.\n"
      "The contents of this message will be destroyed upon viewing: ")

    # Paranoia == Two factor authentication over SMS
    elif int(paranoia) is 3:
      password = password or app.utils.gen_password()

      number, country = app.utils.format_number(number=number)

      sms_content = ("Someone has sent you a Whisper. "
      "Use this code along with the URL sent to your email address to read your whisper: %s" % (password))
      app.utils.send_sms(number=number, country=country, message=sms_content)

      formatted_content = ("Someone has sent you a password protected whisper anonymously. "
      "To open this message, use the confirmation code sent over SMS to (%s) *** %s.\n"
      "The contents of this message will be destroyed upon viewing: " % (number[:3], number[6:]))

    # Paranoia == Two factor authentication via password protection
    elif int(paranoia) is 4:
      pass

    if int(paranoia) > 1:
      app.database.create_disposable(unique_id=message_id, sender=sender, content=content, password=password, db=db)
    
    html = template("email", sender=sender, content=formatted_content, url=url, domain=app.app_config.get("domain"))
    response = app.utils.send_email(address=address, sender=sender, content=html, config=app.app_config)
    app.database.update_stats("sent", paranoia, db)

    return response

  except Exception as e:
    return json.JSONEncoder().encode({
      "success": "false",
      "response": str(e)
    })

@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./whisper/static/')

# Run app locally for testing
#app.run(host="localhost", port=8080, debug=True, reloader=True)

# Run app in production
app.run(port=8080, workers=4, server='gunicorn')