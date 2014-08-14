from whisper import _utils

import inspect
import sqlite3
import json
import os

def init_db():
  
  try:
    db = sqlite3.connect("whisper/db/whisper.db")
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS messages("
      "id PRIMARY KEY,"
      "sender TEXT,"
      "content TEXT,"
      "password TEXT)"
    )

    c.execute("CREATE TABLE IF NOT EXISTS stats("
      "sent INT,"
      "sent_plaintext INT,"
      "sent_disposable INT,"
      "sent_twofactorauth INT,"
      "messages_opened INT)"
    )

    db.commit()
    db.close()
    
  except Exception as e:
    raise Exception("Couldn't initialize DB. ", e)

def init_config():

  if not os.path.exists('./config'):
    open('./config', 'w').write(inspect.cleandoc(
      r'''
      {
        "api_key": "",
        "domain": "yourdomain.com",
        "salt": "%s"
      }''' % _utils.gen_id(10)) + '\n')

  try:
    data = json.load(open("./config", "r"))

  except Exception as e:
    raise Exception("Failed to load config! ", e)

  if data.get("api_key") == "":
    raise Exception("API Key not specified in config. Sign up at http://mailgun.com")

  if data.get("domain") == "yourdomain.com":
    raise Exception("Domain not specified in config.")

  if data.get("salt") == "":
    data['salt'] = _utils.gen_id(10)

    with open("./config", "w") as f:
      json.dump(data, f, indent=2)
  
  return data
