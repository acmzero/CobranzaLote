'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column
from categorias import *
class Ubicacion(Base):
    __tablename__ = "ubicacion"
    ubicacion_id= Column(Integer, primary_key=True)
    numero= Column(Integer)
    calle=Column(String)
    colonia=Column(String)
    municipio=Column(String)
    estado=Column(String)
    
    def __init__(self,numero,calle,colonia,municipio,estado):
      self.numero=numero
      self.calle=calle
      self.colonia=colonia
      self.municipio=municipio
      self.estado=estado
      
    def altas(self,nombre_categoria,numero,calle,colonia,municipio,estado):
      new_ubicacion=Ubicacion(numero,calle,colonia,municipio,estado)
      categoria=Categorias.altas(nombre_categoria)
      new_ubicacion.categorias.extend(categoria)
      session.add(new_ubicacion)
      session.commit()
      
new_ubicacion=Ubicacion
new_ubicacion