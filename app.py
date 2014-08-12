from bottle import Bottle, TEMPLATE_PATH, static_file, request, run
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
def index():
  return dict()

# Todo: Allow the original sender to view and optionally destroy message using cookies.
@app.route('/disposable/<message_id>')
def view_whisper(message_id, db):
  return message_id
  message = app.database.get_disposable(message_id)
  
  return template("disposable", sender=sender, content=content, password=password)

@app.post('/send')
def send_whisper(db):
  address = request.forms.get('address')
  sender = request.forms.get('sender')
  content = request.forms.get('content')
  paranoia = request.forms.get('paranoia')
  password = request.forms.get('password')
  number = request.forms.get('number')

  try:
    password = password or app.utils.gen_password()
    message_id = app.database.create_disposable(sender, content, password, db)    
    url = "http://%s/disposable/%s" % (app.app_config.get("domain"), message_id)

    # Paranoia == Disposable Message
    if int(paranoia) == 2:
      content = ("Someone has sent you a whisper anonymously. "
      "<br />The contents of this message will be destroyed upon viewing: <a href=\"%s\">%s</a>" % (url, url))

    # Paranoia == Two factor authentication over SMS
    elif int(paranoia) == 3:
      number, country = app.utils.format_number(number=number)

      sms_content = ("Someone has sent you a Whisper. "
      "Use this code along with the URL sent to your email address to read your whisper:%%0a %s" % (password))
      app.utils.send_sms(number=number, country=country, message=sms_content)

      content = ("Someone has sent you a password protected whisper anonymously. "
      "To open this message, use the confirmation code sent over SMS to %s."
      "<br />The contents of this message will be destroyed upon viewing: <a href=\"%s\">%s</a>" % (number, url, url))

    # Paranoia == Two factor authentication via password protection
    elif int(paranoia) == 4:
      pass

    return app.utils.send_email(address=address, sender=sender, content=content, config=app.app_config)

  except Exception as e:
    return json.JSONEncoder().encode({
      "success": "false",
      "response": str(e)
    })

@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./whisper/static/')


app.run(host="localhost", port=8080, debug=True, reloader=True)