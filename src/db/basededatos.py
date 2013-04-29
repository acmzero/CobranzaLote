'''
Created on Apr 22, 2013

@author: heli
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import sessionmaker
motor=create_engine("sqlite:///datos.db", echo=False)
Base=declarative_base()
# create tables
#Base.metadata.create_all(motor)
Session = sessionmaker(bind=motor)
session = Session()
