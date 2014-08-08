from bottle import route, run, post, request, template, install, static_file
from bottle_sqlite import SQLitePlugin

import requests
import sqlite3
import utils
import json

install(SQLitePlugin(dbfile="db/whisper.db"))

def _db_init():
  db = sqlite3.connect("db/whisper.db")
  c = db.cursor()

  c.execute("CREATE TABLE IF NOT EXISTS messages("
    "id PRIMARY KEY," 
    "sender TEXT,"
    "content TEXT)"
  )

  db.commit()
  db.close()

@route('/', template="index")
def index():
  return dict()

def create_disposable(sender, content, db):
  unique_id = utils.gen_id()
  c = db.cursor()
  c.execute("INSERT INTO messages "
    "VALUES (?, ?, ?)",
    (unique_id, sender, content))

  db.commit()

  return unique_id

@route('/disposable/<message_id>')
def disposable(message_id, db):
  c = db.cursor()
  c.execute("SELECT sender, content FROM messages WHERE id=?", (message_id,))

  result = c.fetchone()
  if result is None:
    return template("disposable_expired")
  
  sender, content = result

  c.execute("DELETE FROM messages where id=?", (message_id,))
  db.commit()

  return template("disposable", sender=sender, content=content)


  return dict(sender=sender, content=content)

@post('/send')
def send_email(db):
  address = request.forms.get('address')
  sender = request.forms.get('sender')
  content = request.forms.get('content')
  paranoia = request.forms.get('paranoia')

  if int(paranoia) == 2:
    try:
      message_id = create_disposable(sender, content, db)
      
      #url = "http://whisper.email/disposable/%s" % message_id
      url = "http://%s/disposable/%s" % (config.get("domain"), message_id)
      content = "Someone has sent you a whisper anonymously.<br />The contents of this message will be destroyed upon viewing: <a href=\"%s\">%s</a>" % (url, url)

    except Exception as e:
      return json.JSONEncoder().encode({
        "success": "false",
        "response": str(e)
      })

  api = "https://api.mailgun.net/v2/%s/messages" % config.get("domain")
  auth = ("api", config.get("api_key"))
  
  data = { 
    "from": "Whisper <whisper@%s>" % config.get("domain"),
    "to": "<%s>" % address,
    "subject": "Whisper from %s, anonymously." % sender,
    "html": content
  }

  response = requests.post(url=api, auth=auth, data=data)
  json_data = json.loads(response.text)

  if json_data['message'] == "Queued. Thank you.":
    return json.JSONEncoder().encode({
      "success": "true"
    })

  else:
    return json.JSONEncoder().encode({
      "success": "false",
      "response": r['message']
    })

@route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./static/')

_db_init()
config = utils.config()
run(host='0.0.0.0', port=8080, debug=True, reloader=True)