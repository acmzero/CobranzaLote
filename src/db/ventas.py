'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column
from clientes import *
from sqlalchemy.orm import backref
from sqlalchemy.types import Date

class Venta(Base):
    __tablename__ = "venta"
    venta_id= Column(Integer, primary_key=True)
    fecha=Column(Date)
    folio=Column(String)
    cliente_id=Column(Integer, ForeignKey("cliente.cliente_id"))
    cliente=relationship("Cliente", backref=backref("venta"))
    
    def __init__(self,fecha,folio):
      self.fecha=fecha
      self.folio=folio
      
    