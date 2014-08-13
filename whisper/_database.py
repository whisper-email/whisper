from whisper import _utils
import sqlite3

def create_disposable(sender, content, password, db):
  unique_id = _utils.gen_id()
  c = db.cursor()
  c.execute("INSERT INTO messages "
    "VALUES (?, ?, ?, ?)",
    (unique_id, sender, content, password))

  db.commit()

  return unique_id

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
  c.execute("DELETE FROM messages where id=?", (message_id,))
  
  db.commit()