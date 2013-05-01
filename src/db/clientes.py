'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column
from categorias import *

class Cliente(Base):
  __tablename__ = "cliente"
  cliente_id= Column(Integer, primary_key=True)
  nombre_completo= Column(String)
  nombre=Column(String)
  apellidos=Column(String)
  categoria_id=Column(Integer, ForeignKey("categoria.categoria_id"))
  categoria=relationship("Categoria", backref=backref("cliente"))
    
  
    