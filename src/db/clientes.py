'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column
from categorias import *

class Clientes(Base):
  __tablename__ = "clientes"
  cliente_id= Column(Integer, primary_key=True)
  nombre_completo= Column(String)
  nombre=Column(String)
  apellidos=Column(String)
  categoria_id=Column(Integer, ForeignKey("categorias.categorias_id"))
  categoria=relationship("Categorias", backref=backref("clientes"))
    
  def __init__(self,nombre,nombre_completo,apellidos):
    self.nombre=nombre
    self.nombre_completo=nombre_completo
    self.apellidos=apellidos
    
    