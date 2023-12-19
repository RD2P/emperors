from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

load_dotenv()

engine = create_engine(os.getenv("DB_CONNECTION_STRING"))

def get_emperors_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM emperors"))
    result_dicts = []
    for row in result.mappings().all():
      result_dicts.append(dict(row))

    return result_dicts