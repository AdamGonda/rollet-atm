from sqlalchemy import Column, Integer, DateTime, String
from flask_sqlalchemy import SQLAlchemy
import os

SUCCESS = 'Success'
FAILURE = 'Failure'

def get_db_url():
    return f"postgresql+psycopg2://{os.environ['DB_USER_NAME']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"


db = SQLAlchemy()


# tables
class Bill(db.Model):
    __tablename__ = 'bill'

    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    quantity = Column(Integer)


class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    success_status = Column(String)
    amount = Column(Integer)





