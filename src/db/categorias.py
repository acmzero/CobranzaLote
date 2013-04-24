'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column
from ubicacion import *
from sqlalchemy.orm import backref

class Categorias(Base):
    __tablename__ = "categorias"
    categoria_id= Column(Integer, primary_key=True)
    nombre=Column(String)
    ubicacion_id=relationship("Ubicacion", backref=backref("ubicacion"))
    