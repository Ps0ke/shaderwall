from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import datetime
from config import connection_url
import random
import string

def generate_authcode():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))

Base = declarative_base()
class Shader(Base):
    __tablename__ = 'shader'
    id = Column(Integer, primary_key=True)
    source = Column(Text)
    authcode = Column(String(32), default=generate_authcode)
    created = Column(DateTime, default=datetime.datetime.now)
    updated = Column(DateTime, default=datetime.datetime.now)
    views = Column(Integer, default=0)

def setup_db():
    global engine
    engine = create_engine(connection_url, pool_recycle=14400)
    Base.metadata.create_all(engine)

def db_session():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session
