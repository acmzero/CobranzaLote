'''
Created on May 1, 2013

@author: heli
'''
from basededatos import *
from sqlalchemy import Column, Integer, String, Float, DateTime, event

from ubicacion import *
from sqlalchemy.orm import backref
from camelot.core.orm import Entity
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm.relationships import OneToMany, ManyToOne, OneToOne
from sqlalchemy.types import Date
import datetime

class Categoria(Entity):
  __tablename__ = "categoria"
  nombre = Column(String)
  clientes = OneToMany("Cliente")
  ubicacion = ManyToOne("Ubicacion")

    
  def __unicode__(self):
    return self.nombre
  
  class Admin(EntityAdmin):
    form_size = (420, 320)
    verbose_name = "Oficina"
    list_display = ["nombre"]
    form_display = list_display + ["ubicacion", 'clientes']
    
class Cliente(Entity):
  __tablename__ = "cliente"
  nombre_completo = Column(String)
  nombre = Column(String)
  apellidos = Column(String)
  categoria = ManyToOne("Categoria")
  pagos = OneToMany("Pagos")
  ventas = OneToMany("Venta")
  referente = ManyToOne("Cliente")
  comision = Column(Float)
  def __unicode__(self):
    return self.nombre_completo
  
  class Admin(EntityAdmin):
    form_size = (420, 320)
    list_display = ['nombre_completo']
    form_display = ["nombre_completo", "referente", "comision", "pagos"]
    
class DetalleVenta(Entity):
  __tablename__ = "detalle_ventas"
  linea = Column(Integer)
  cantidad = Column(Integer)
  precio=Column(Float)
  producto = ManyToOne("Productos")
  venta = ManyToOne("Venta")
  def __unicode__(self):
    return str(self.cantidad)
  
  
  def _gettotal(self):
    return self.cantidad*self.precio
    
  @property
  def total(self):
    return int(self.cantidad)*float(self.precio) or 0
  

  def get_precio(self):
    if self.producto==None:
      return self.precio
    else:
      if self.precio==None:
        self.precio=self.producto.precios[0].precio
        return self.precio
      else:
        return self.precio
  
  def set_precio(self,precio):
    self.precio=precio or 0
  
  _precio=property(get_precio,set_precio)
  
  @property
  def _producto(self):
    if self.producto!=None:
      self.precio=self.producto.precios[0].precio
    return self.venta.cliente
  class Admin(EntityAdmin):
    # form_size = (400,200)
    verbose_display = "Detalle de Ventas"
    list_display = ["linea", "producto", "cantidad", "_precio", "total"]
    form_display = ["linea", "producto", "cantidad", "_precio", "total","_producto"]
    field_attributes={"_precio":{"editable":True},
                      "_producto":{"name":"PROasdAs"}}
    
    
    
class Pagos(Entity):
  __tablename__ = "pagos"
  fecha = Column(Date)
  cantidad = Column(Float)
  cliente = ManyToOne("Cliente")
  
  def __unicode__(self):
    return str(self.cantidad) or "No Definido"
  
  class Admin(EntityAdmin):
    # form_size = (400,200)
    list_display = ["fecha", "cantidad"]
    form_display = ["fecha", "cantidad"]
    
class Ubicacion(Entity):
  __tablename__ = "ubicacion"
  # ubicacion_id= Column(Integer, primary_key=True)
  numero = Column(Integer)
  calle = Column(String)
  colonia = Column(String)
  ciudad = Column(String)
  estado = Column(String)
  categorias = OneToMany("Categoria")
  # descripcion=calle+" "+numero+", "+ciudad
    
  def __unicode__(self):
    return self.ciudad or "No Definido"
  
  class Admin(EntityAdmin):
    # form_size = (400,200)
    verbose_name = "Ubicacion"
    list_display = ["ciudad"]
    form_display = ["calle", "numero", "colonia", "ciudad", "estado"]
    
class Productos(Entity):
  __tablename__ = "productos"
  nombre = Column(String, nullable=False)
  descripcion = Column(String)
  sn = Column(String)
  lineas = OneToMany("DetalleVenta")
  precios = OneToMany("Precios")
  
  def __unicode__(self):
    return self.nombre or "No Definido"
  
  class Admin(EntityAdmin):
    # form_size = (400,200)
    verbose_name = "Producto"
    list_display = ["nombre"]
    form_display = ["nombre", "sn", "descripcion", "precios"]


class Precios(Entity):
  __tablename__ = "precios"
  fecha = Column(Date)
  precio = Column(Float)
  producto = ManyToOne("Productos")
    
  def __unicode__(self):
    return self.precio or "No Definido"
  
  class Admin(EntityAdmin):
    # form_size = (400,200)
    verbose_name = "Precio"
    list_display = ["fecha", "precio"]
    form_display = ["fecha", "precio"]

class Venta(Entity):
  __tablename__ = "venta"
  fecha = Column(DateTime, default=datetime.datetime.now())
  folio = Column(String)
  cliente = ManyToOne("Cliente")  
  lineas = OneToMany("DetalleVenta")
  escanear = "Escanear Producto Aqui"
  def __unicode__(self):
    return str(self.fecha) or "No Definido"
  
  class Admin(EntityAdmin):
    # form_size = (400,200)
    verbose_name = "Venta"
    list_display = ["fecha", "folio", "cliente"]
    form_display = list_display + ["escanear", "lineas"]
#    field_attributes = {"escanear": {"editable":True}}
    
    
def poner_precio(target, value, oldValue, initiator):
  print "target: " + str(target) + " Value: " + str(value) + " initiator: " + initiator
  

def total_linea(target, value, initiator):
  pass

# event.listen(DetalleVenta.producto, "set", poner_precio) 
