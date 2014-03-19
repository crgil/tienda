# Create your views here.

from principal.models import producto
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from principal.forms import ProductoForm
from django.contrib.auth.models import User

def inicio(request):
	html = "<html><body>inicio.html</body></html>"
	return HttpResponse(html)

def usuario(request):
	usuarios = User.objects.all()
	producto = producto.objects.all()
	return render_to_response('usuarios.html', {'usuarios':usuarios, 'productos':productos})

def lista_productos(request):
	productos = producto.objects.all()
	return render_to_response('productos.html',{'lista':productos}, context_instance=RequestContext(request))



def agregar_producto(request):
	if request.method == 'POST':
		formulario = ProductoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/tienda')
	else:
		formulario = ProductoForm()
	return render_to_response('productoform.html', {'formulario':formulario}, context_instance=RequestContext(request))