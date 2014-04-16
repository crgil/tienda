#encoding:utf-8
from django.db import models
from django.contrib import admin
from datetime import datetime    
from django.contrib.auth.models import User, check_password

# Create your models here.
class tienda(models.Model):
	nombre_tienda = models.CharField(max_length = 200)
	direccion = models.CharField(max_length = 300)
	telefono = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50)
	nit = models.IntegerField(default = 0)
	
	def __unicode__(self):
		return self.nombre_tienda
		return self.direccion
		return self.telefono
		return self.email
		return self.nit


	
class sucursal(models.Model):
	nombre_sucursal = models.CharField(max_length=200)
	direccion = models.CharField(max_length=300)
	telefono = models.CharField(max_length = 50)
	emal = models.CharField(max_length=50)
	no_tienda = models.ForeignKey(tienda)

	def __unicode__(self):
		return self.nombre_sucursal
		return self.direccion
		return self.telefono
		return self.emal
		return self.no_tienda
	
class cargo (models.Model):
	nombre_cargo = models.CharField(max_length = 100)
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre_cargo
		return self.descripcion
	
class empleado(models.Model):
	nombre_emp = models.CharField (max_length = 100)
	apellido_emp = models.CharField(max_length = 100)
	tipo_id = models.IntegerField (default = 0)
	orden_id = models.CharField(max_length = 20)
	registro_id = models.IntegerField(default=0)
	direccion = models.CharField(max_length = 300)
	telefono = models.CharField(max_length = 50)
	no_sucursal = models.ForeignKey(sucursal)
	cargo = models.ForeignKey(cargo)

	def __unicode__(self):
		return self.nombre_emp
		return self.apellido_emp
		return self.tipo_id
		return self.orden_id
		return self.registro_id
		return self.direccion
		return self.telefono
		return self.no_sucursal
		return self.cargo
	
class producto (models.Model):
	codigoproducto = models.CharField(max_length = 200)
	nombre_prod = models.CharField(max_length = 200)
	descripcion = models.CharField(max_length = 300)
	marca = models.CharField(max_length = 200)
	precio_u = models.DecimalField(max_digits=10, decimal_places=2)
	existencia = models.IntegerField(default = 0)
	status = models.IntegerField(default = 1)

	def __unicode__(self):
		return self.nombre_prod
		return self.descripcion
		return self.marca
		return self.precio_u

class cliente (models.Model):
	nombre_cliente = models.CharField(max_length = 100)
	apellido_cliente = models.CharField(max_length = 100)
	nit = models.IntegerField()
	direccion = models.CharField(max_length = 300)
	telefono = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.nombre_cliente
		return self.apellido_cliente
		return self.nit
		return self.direccion
		return self.telefono

class proveedor (models.Model):
	nombre_proveedor = models.CharField(max_length = 200)
	nit = models.IntegerField()
	direccion = models.CharField(max_length = 300)
	telefono = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.nombre_proveedor
		return self.nit
		return self.direccion
		return self.telefono
	
class factura (models.Model):
	serie = models.CharField(max_length = 20)
	no_factura = models.IntegerField()
	fecha_factura = models.DateTimeField('Fecha Factura', default=datetime.now())
	vendedor = models.ForeignKey(empleado)
	sucursal = models.ForeignKey(sucursal)
	estado = models.IntegerField(default=1)
	cliente = models.ForeignKey(cliente)
	total = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.serie
		return self.no_factura
		return self.fecha_factura
		return self.vendedor
		return self.sucursal
		return self.estado
		return self.cliente
		return self.total
	
class detalle_factura (models.Model):
	factura_venta = models.ForeignKey(factura)
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField ()
	precio_u_venta = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.factura_venta
		return self.producto
		return self.cantidad
		return self.precio_u_venta

class detalle_facturaInline(admin.TabularInline):
    model = detalle_factura

class facturaAdmin(admin.ModelAdmin):
    inlines = (detalle_facturaInline,)

class credito_venta (models.Model):
	factura_venta = models.ForeignKey(factura)
	fecha_credito_venta = models.DateTimeField('Fecha credito')
	cant_pagos = models.IntegerField()
	monto = models.DecimalField(max_digits=10, decimal_places=2)
	saldo = models.DecimalField(max_digits=10, decimal_places=2)
	
	def __unicode__(self):
		return self.factura_venta
		return self.fecha_credito_venta
		return self.cant_pagos
		return self.monto
		return self.saldo

class Abono (models.Model):
	credito = models.ForeignKey(credito_venta)
	fecha_pago = models.DateTimeField('Fecha credito')
	monto_pago = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.credito
		return self.fecha_pago
		return self.monto_pago

class compra (models.Model):
	serie = models.CharField(max_length = 20)
	no_factura = models.IntegerField()
	fecha_compra = models.DateTimeField('Fecha Factura')
	sucursal = models.ForeignKey(sucursal)
	estado = models.IntegerField()
	proveedor = models.ForeignKey(proveedor)
	total = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.serie
		return self.no_factura
		return self.fecha_compra
		return self.sucursal
		return self.estado
		return self.proveedor
		return self.total

class detalle_compra (models.Model):
	factura_compra = models.ForeignKey(compra)
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField ()
	precio_u_compra = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.factura_compra
		return self.producto
		return self.cantidad
		return self.precio_u_compra


class credito_compra (models.Model):
	factura_compra = models.ForeignKey(compra)
	fecha_credito_compra = models.DateTimeField('Fecha credito')
	cant_pagos = models.IntegerField()
	monto = models.DecimalField(max_digits=10, decimal_places=2)
	saldo = models.DecimalField(max_digits=10, decimal_places=2)
	
	def __unicode__(self):
		return self.factura_compra
		return self.fecha_credito_compra
		return self.cant_pagos
		return self.monto
		return self.saldo

class Abono_compra (models.Model):
	credito = models.ForeignKey(credito_compra)
	fecha_pago = models.DateTimeField('Fecha credito')
	monto_pago = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.credito
		return self.fecha_pago
		return self.monto_pago
