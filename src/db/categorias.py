'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column, ForeignKey
from ubicacion import *
from sqlalchemy.orm import backref

class Categorias(Base):
    __tablename__ = "categorias"
    categoria_id= Column(Integer, primary_key=True)
    nombre=Column(String)
    ubicacion_id=Column(Integer, ForeignKey("ubicacion.ubicacion_id"))
    ubicacion=relationship("Ubicacion", backref=backref("categorias"))
    
    def __init__(self,nombre):
      self.nombre=nombre
      
    def altas(self,nombre):
      categoria=[Categorias(nombre)]