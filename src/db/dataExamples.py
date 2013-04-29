'''
Created on Apr 28, 2013

@author: heli
'''

import initDataBase
from clientes import Cliente
from categorias import Categoria
import lineas,pagos,precios,productos,ubicacion,ventas
from db.basededatos import session

#Borrar registros previos
#session.execute(Cliente.delete().where(Cliente.nombre.like("%"))
for i in session.query(Cliente):
  #print "Borrando",i.nombre
  session.delete(i)
  
for i in session.query(Categoria):
  session.delete(i)
session.commit()
  

#Registrar Dos clientes
clientes=[]
clienteA=Cliente("Pedro", "Pedro Palacios", "Palacios")
clienteB=Cliente("Heli","Heli Villarreal","Villarreal")
clientes.append(clienteA)
clientes.append(clienteB)

categoriaA=Categoria("ITSSP")

print dir(clienteA)
clienteA.categoria=categoriaA
#clienteB.cliente.extends(categoriaA)
categoriaA.cliente.extend([clienteB])

session.add_all(clientes)
session.add(categoriaA)
session.commit()

res=session.query(Cliente)

for r in res:
  print "Cliente",r.nombre
  
