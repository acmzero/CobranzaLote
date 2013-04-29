'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column, ForeignKey
from ubicacion import *
from sqlalchemy.orm import backref

class Categoria(Base):
    __tablename__ = "categoria"
    categoria_id= Column(Integer, primary_key=True)
    nombre=Column(String)
    ubicacion_id=Column(Integer, ForeignKey("ubicacion.ubicacion_id"))
    ubicacion=relationship("Ubicacion", backref=backref("categoria"))
    
    def __init__(self,nombre=None):
      self.nombre=nombre
      
    def altas(self,nombre):
      categoria=[Categoria(nombre)]
      return categoria