from primerProyecto.wsgi import *
'''
from apps.users.models import Domicilio

#listamos
lista1 = Domicilio.objects.all()
print(lista1)

#Insertar
dom = Domicilio()
dom.addres = 'pruebadom1'
dom.save()

#Editar
dom = Domicilio.objects.get(id = 1)
print(dom.addres)
dom.addres ='pruebadom1.1'

#Eliminar
dom = Domicilio.objects.get(id = 1)
print(dom.addres)
dom.delete()

#Listado con filtro
listaFiltro = Domicilio.objectos.filter(addres__contains='1')'''