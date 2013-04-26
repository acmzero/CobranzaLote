'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column
from clientes import *
from sqlalchemy.orm import backref
from sqlalchemy.types import Date

class Ventas(Base):
    __tablename__ = "ventas"
    venta_id= Column(Integer, primary_key=True)
    fecha=Column(Date)
    folio=Column(String)
    cliente_id=Column(Integer, ForeignKey("clientes.clientes_id"))
    cliente=relationship("Clientes", backref=backref("ventas"))
    
    def __init__(self,fecha,folio):
      self.fecha=fecha
      self.folio=folio
      
    