
from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _
from db.modelo import Categoria,Cliente,Lineas,Pagos,Ubicacion,Venta
class MyApplicationAdmin(ApplicationAdmin):
  
    name = 'Cobranza'
    application_url = '-'
    help_url = '-'
    author = '-'
    domain = '-'
    
    def get_sections(self):
        from camelot.model.memento import Memento
        from camelot.model.i18n import Translation
        return [ Section( _('My classes'),
                          self,
                          Icon('tango/22x22/apps/system-users.png'),
                          items = [Categoria,Cliente,Venta] ),
                 Section( _('Configuration'),
                          self,
                          Icon('tango/22x22/categories/preferences-system.png'),
                          items = [Memento, Translation] )
                ]
    