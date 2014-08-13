import requests
import random
import string
import json

def gen_id(length=10):
  chars = string.ascii_letters + string.digits

  return "".join([random.choice(chars) for x in range(length)])

def gen_password():
  chars = string.digits
  
  password = "".join([random.choice(chars) for x in range(6)])
  password = "%s-%s" % (password[:3], password[3:])
  return password
  
def format_number(number):
  # Strip unnecessary characters, leaving just the digits.
  stripped = string.punctuation + " "
  number.translate(number.maketrans(dict(zip(stripped, ["" for x in stripped]))))

  # Check if the number contains a country code, else assume US or fail if less than 9 digits.
  if number.isdigit():

    if len(number) == 11:
      return (number[1:], "united states") if number[0] == "1" else (number[1:], "international")
    
    elif len(number) == 10:
      return (number, "united states")
  
  else:
    raise Exception("Not a valid phone number.")

def send_sms(number, country, message):
  if country == "united states":
    api = "http://textbelt.com/text"

  elif country == "canada":
    # Note: Not currently possible to differentiate between U.S. and Canadian numbers. 
    api = "http://textbelt.com/canada"

  elif country == "international":
    api = "http://textbelt.com/intl"

  data = {
    "number": number,
    "message": message
  }

  response = requests.post(api, data=data)

  return (number, response.text)

def send_email(address, sender, content, config):
  api = "https://api.mailgun.net/v2/%s/messages" % (config.get("domain"))
  auth = ("api", config.get("api_key"))
  
  data = { 
    "from": "Whisper <whisper@%s>" % (config.get("domain")),
    "to": "<%s>" % (address),
    "subject": "Whisper from %s, anonymously." % (sender),
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