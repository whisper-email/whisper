import inspect
import random
import string
import json
import os

def gen_id(length=10):
  chars = string.ascii_letters + string.digits

  return "".join([random.choice(chars) for x in range(length)])

def config():
  def _init_config():
    if not os.path.exists('./config'):
      open('./config', 'w').write(inspect.cleandoc(
        r'''
        {
          "api_key": "",
          "domain": "yourdomain.com",
          "salt": "%s"
        }''' % gen_id(10)) + '\n')

  _init_config()

  try:
    return json.load(open("config", "r"))
  
  except Exception as e:
    raise Exception("Failed to load config! ", e)
