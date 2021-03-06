from whisper import _database, _init, _utils
import unittest
import sqlite3
import random
import json

class DatabaseTestCase(unittest.TestCase):
  def setUp(self):
    _init.init_db()
    self.db = sqlite3.connect("whisper/db/whisper.db")

  def test_create_disposable(self):
    # Generate a random ID to test disposable creation
    random_ID = str(round(random.random() * 100000))
    _database.create_disposable(random_ID, "sender", "content", "password", self.db)

    # Grab message from DB
    c = self.db.cursor()
    c.execute("SELECT sender, content, password FROM messages WHERE id=?", (random_ID,))
    result = c.fetchone()

    sender, content, password = result
    self.assertEqual((sender, content, password), ("sender", "content", "password"))

  def test_retrieve_disposable(self):
    # Generate a random ID to test disposable retrieval
    random_ID = str(round(random.random() * 100000))

    # Insert message into DB
    c = self.db.cursor()
    c.execute("INSERT INTO messages "
      "VALUES (?, ?, ?, ?)",
      (random_ID, "sender", "content", "password")
    )

    self.db.commit()
    
    message = _database.get_disposable(random_ID, self.db)
    self.assertEqual(message, ("sender", "content", "password"))

  def test_delete_disposable(self):
    # Generate a random ID to test disposable deletion
    random_ID = str(round(random.random() * 100000))

    # Insert message into DB
    c = self.db.cursor()
    c.execute("INSERT INTO messages "
      "VALUES (?, ?, ?, ?)",
      (random_ID, "sender", "content", "password")
    )

    self.db.commit()

    _database.delete_disposable(random_ID, self.db)
    
    message = _database.get_disposable(random_ID, self.db)
    self.assertEqual(message, None)

  def test_get_stats(self):
    c = self.db.cursor()
    c.execute("INSERT OR IGNORE INTO stats "
      "VALUES (1, 0, 0, 0, 0 ,0)"
    )

    self.db.commit()

    stats = _database.get_stats(self.db)
    self.assertEqual(stats, (1, 0, 0, 0, 0, 0))


class InitTestCase(unittest.TestCase):  
  def test_init_db(self):
    _init.init_db()
    db = sqlite3.connect("whisper/db/whisper.db")
    
    self.assertIsInstance(db, sqlite3.Connection)

  def test_init_config(self):
    with self.assertRaises(Exception) as e:
      try: 
        _init.init_config()

      except Exception:
        self.assertEqual(e.msg, "API Key not specified in config. Sign up at http://mailgun.com")

    with open("./config", "r+") as f:
      self.data = json.load(f)
      self.data['api_key'] = "testapikey"
      json.dump(self.data, f, indent=2)

    with self.assertRaises(Exception) as e:
      try: 
        _init.init_config()

      except Exception:
        self.assertEqual(e.msg, "Domain not specified in config.")

    with open("./config", "w") as f:
      self.data['domain'] = "testunittests.com"
      json.dump(self.data, f, indent=2)

    config = _init.init_config()  
    self.assertIsInstance(config, dict)

class UtilsTestCase(unittest.TestCase):
  def test_gen_id(self):
    ID = _utils.gen_id()

    # Returns a 10 character string
    self.assertTrue(len(ID) is 10)
    self.assertIsInstance(ID, str)

    # No duplicates
    ID_list = [_utils.gen_id() for x in range(10)]
    self.assertTrue(len(set(ID_list)) is 10)

  def test_gen_password(self):
    password = _utils.gen_password()

    # Returns a 7 character string
    self.assertTrue(len(password) is 7)
    self.assertIsInstance(password, str)

  def test_format_number(self):
    formatted_number = _utils.format_number("1 (888) 555-5555")
    self.assertEqual(formatted_number, ('8885555555', 'united states'))

  @unittest.skip("This cannot be safely tested without spamming.")
  def test_send_sms(self):
    #response = _utils.send_sms(None, None, None)
    pass

  @unittest.skip("This cannot be tested without an API key, or tested regularly without spamming.")
  def test_send_email(self):
    #response = _utils.send_email(None, None, None, None)
    pass
