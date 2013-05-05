
from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _
from db.modelo import Categoria,Cliente,DetalleVenta,Pagos,Ubicacion,Venta,Productos
class MyApplicationAdmin(ApplicationAdmin):
  
    name = 'Cobranza'
    application_url = '-'
    help_url = '-'
    author = '-'
    domain = '-'
    
    def get_sections(self):
        from camelot.model.memento import Memento
        from camelot.model.i18n import Translation
        return [ Section( _('Menu'),
                          self,
                          Icon('tango/22x22/apps/system-users.png'),
                          items = [Categoria,Venta,Productos] ),
#                 Section( _('Configuration'),
#                          self,
#                          Icon('tango/22x22/categories/preferences-system.png'),
#                          items = [Memento, Translation] )
                ]
    def get_main_menu(self):
      pass
#      return ApplicationAdmin.get_main_menu(self)
    