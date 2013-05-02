'''
Created on May 1, 2013

@author: heli
'''
from basededatos import *
from sqlalchemy import Column, Integer, String,Float

from ubicacion import *
from sqlalchemy.orm import backref
from camelot.core.orm import Entity
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm.relationships import OneToMany, ManyToOne, OneToOne
from sqlalchemy.types import Date

class Categoria(Entity):
  __tablename__ = "categoria"
  nombre=Column(String)
  clientes=OneToMany("Cliente")
  ubicacion=ManyToOne("Ubicacion")

    
  def __unicode__(self):
    return self.nombre
  
  class Admin( EntityAdmin ):
    #form_size = (400,200)
    verbose_name="Oficina"
    list_display = ["nombre"]
    form_display = list_display + ["ubicacion",'clientes']
    
class Cliente(Entity):
  __tablename__ = "cliente"
  nombre_completo= Column(String)
  nombre=Column(String)
  apellidos=Column(String)
  categoria=ManyToOne("Categoria")
  pagos=OneToMany("Pagos")
  ventas=OneToMany("Venta")
  def __unicode__(self):
    return self.nombre_completo
  
  class Admin( EntityAdmin ):
    form_size = (400,200)
    list_display = ['nombre_completo',"categoria"]
    form_display = ["nombre_completo", "pagos"]
    
class Lineas(Entity):
  __tablename__ = "lineas"
  linea=Column(Integer)
  cantidad=Column(Integer)
  precio=Column(Float)
  total=Column(Float)
  producto=ManyToOne("Productos")
  venta=ManyToOne("Venta")
  def __unicode__(self):
    return str(self.cantidad)
  
  class Admin( EntityAdmin ):
    #form_size = (400,200)
    verbose_display="Detalle de Ventas"
    list_display = ["linea","producto","cantidad","precio","total"]
    form_display=["linea","producto","cantidad","precio","total"]
    
class Pagos(Entity):
  __tablename__ = "pagos"
  fecha=Column(Date,nullable=False)
  cantidad=Column(Float, nullable=False)
  cliente=ManyToOne("Cliente")
  
  def __unicode__(self):
    return str(self.cantidad) or "No Definido"
  
  class Admin( EntityAdmin ):
    #form_size = (400,200)
    list_display = ["fecha","cantidad"]
    form_display=["fecha","cantidad"]
    
class Ubicacion(Entity):
  __tablename__ = "ubicacion"
  #ubicacion_id= Column(Integer, primary_key=True)
  numero= Column(Integer)
  calle=Column(String)
  colonia=Column(String)
  ciudad=Column(String)
  estado=Column(String)
  categorias=OneToMany("Categoria")
  #descripcion=calle+" "+numero+", "+ciudad
    
  def __unicode__(self):
    return self.ciudad or "No Definido"
  
  class Admin( EntityAdmin ):
    #form_size = (400,200)
    verbose_name="Ubicacion"
    list_display = ["ciudad"]
    form_display = ["calle","numero","colonia","ciudad","estado"]
    
class Productos(Entity):
  __tablename__ = "productos"
  nombre= Column(String)
  descripcion=Column(String)
  sn=Column(String)
  lineas=OneToMany("Lineas")
  precios=OneToMany("Precios")
  
  def __unicode__(self):
    return self.nombre or "No Definido"
  
  class Admin( EntityAdmin ):
    #form_size = (400,200)
    verbose_name="Producto"
    list_display = ["nombre"]
    form_display = ["nombre","sn","descripcion","precios"]


class Precios(Entity):
  __tablename__ = "precios"
  fecha=Column(Date)
  precio=Column(Float)
  producto=ManyToOne("Productos")
    
  def __unicode__(self):
    return self.precio or "No Definido"
  
  class Admin( EntityAdmin ):
    #form_size = (400,200)
    verbose_name="Precio"
    list_display = ["fecha","precio"]
    form_display = ["fecha","precio"]

class Venta(Entity):
  __tablename__ = "venta"
  fecha=Column(Date)
  folio=Column(String)
  cliente=ManyToOne("Cliente")  
  lineas=OneToMany("Lineas")
  def __unicode__(self):
    return str(self.fecha) or "No Definido"
  
  class Admin( EntityAdmin ):
    #form_size = (400,200)
    verbose_name="Venta"
    list_display = ["fecha","folio","cliente"]
    form_display = list_display  +["lineas"]
