#encoding:utf-8
from principal.models import tienda
from principal.models import sucursal
from principal.models import cargo
from principal.models import empleado
from principal.models import producto
from principal.models import cliente
from principal.models import proveedor
from principal.models import factura
from principal.models import detalle_factura
from principal.models import credito_venta
from principal.models import Abono
from principal.models import compra
from principal.models import detalle_compra
from principal.models import credito_compra
from principal.models import Abono_compra
from django.contrib import admin
from principal.models import detalle_facturaInline
from principal.models import facturaAdmin

admin.site.register(tienda)
admin.site.register(sucursal)
admin.site.register(cargo)
admin.site.register(empleado)
admin.site.register(producto)
admin.site.register(cliente)
admin.site.register(proveedor)
#admin.site.register(factura)
admin.site.register(detalle_factura)
admin.site.register(credito_venta)
admin.site.register(Abono)
admin.site.register(compra)
admin.site.register(detalle_compra)
admin.site.register(credito_compra)
admin.site.register(Abono_compra)
admin.site.register(factura, facturaAdmin)