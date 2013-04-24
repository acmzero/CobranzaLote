'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column

class Ubicacion(Base):
    __tablename__ = "ubicacion"
    ubicacion_id= Column(Integer, primary_key=True)
    numero= Column(Integer)
    calle=Column(String)
    colonia=Column(String)
    municipio=Column(String)
    estado=Column(String)