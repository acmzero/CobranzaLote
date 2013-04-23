'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column

class Productos(Base):
    __tablename__ = "productos"
    producto_id= Column(Integer, primary_key=True)
    nombre= Column(String)
    descripcion=Column(String)
    sn=Column(String)