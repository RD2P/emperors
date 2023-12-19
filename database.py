from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

load_dotenv()

host=os.getenv("DATABASE_HOST")
user=os.getenv("DATABASE_USERNAME")
passwd=os.getenv("DATABASE_PASSWORD")
db=os.getenv("DATABASE")

db_connection_string = f"mysql+mysqlconnector://{user}:{passwd}@{host}/{db}"

engine = create_engine(db_connection_string)

def get_emperors_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM emperors"))
    result_dicts = []
    for row in result.mappings().all():
      result_dicts.append(dict(row))

    return result_dicts