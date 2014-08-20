import sqlite3

def create_disposable(unique_id, sender, content, password, db):
  c = db.cursor()
  c.execute("INSERT INTO messages "
    "VALUES (?, ?, ?, ?)",
    (unique_id, sender, content, password)
  )

  db.commit()

def get_disposable(message_id, db):
  c = db.cursor()
  c.execute("SELECT sender, content, password FROM messages WHERE id=?", (message_id,))

  result = c.fetchone()

  if result is None:
    return None
  
  sender, content, password = result

  return (sender, content, password)

def delete_disposable(message_id, db):
  c = db.cursor()
  c.execute("DELETE FROM messages WHERE id=?", (message_id,))
  
  db.commit()

def get_stats(db):
  c = db.cursor()
  c = db.execute("SELECT sent, messages_opened FROM stats WHERE id = 1")
  
  return c.fetchone()

def update_stats(*args):
  event, *args, db = args

  c = db.cursor()

  c.execute("INSERT OR IGNORE INTO stats "
    "VALUES (1, 0, 0, 0, 0 ,0)"
  )

  c.execute("INSERT OR IGNORE INTO stats_historical "
    "VALUES(date('now'), 0, 0, 0, 0, 0)"
  )

  if event is "sent":
    paranoia = int(args[0])

    increment = {
      "sent": 1,
      "plaintext": 1 if paranoia is 1 else 0,
      "disposable": 1 if paranoia is 2 else 0,
      "twofactorauth": 1 if paranoia is 3 else 0
    }

    c.execute("UPDATE stats "
      "SET sent = sent + ?, sent_plaintext = sent_plaintext + ?, sent_disposable = sent_disposable + ?, sent_twofactorauth = sent_twofactorauth + ? "
      "WHERE id = 1 ",
      (increment['sent'], increment['plaintext'], increment['disposable'], increment['twofactorauth'])
    )

    c.execute("UPDATE stats_historical "
      "SET sent = sent + ?, sent_plaintext = sent_plaintext + ?, sent_disposable = sent_disposable + ?, sent_twofactorauth = sent_twofactorauth + ? "
      "WHERE date = date('now')",
      (increment['sent'], increment['plaintext'], increment['disposable'], increment['twofactorauth'])
    )

  elif event is "opened":
    c.execute("UPDATE stats "
      "SET messages_opened=messages_opened + 1 "
      "WHERE id = 1"
    )

    c.execute("UPDATE stats_historical "
      "SET messages_opened=messages_opened + 1 "
      "WHERE date = date('now')"
    )

  db.commit()