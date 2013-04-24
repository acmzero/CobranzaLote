'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column
from clientes import *
from sqlalchemy.orm import backref
from sqlalchemy.types import Date

class Pagos(Base):
    __tablename__ = "pagos"
    pago_id= Column(Integer, primary_key=True)
    fecha=Column(Date)
    cantidad=Column(Integer)
    cliente_id=relationship("Clientes", backref=backref("cliente"))
    