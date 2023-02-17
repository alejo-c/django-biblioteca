from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

from .models import libro
from .forms import LibroForm


# Create your views here.
def inicio(request):
	return render(request, 'libros/index.html')


def libros(request):
	libros = libro.objects.all()
	return render(request, 'libros/libros.html', {'libros': libros})


def crear(request):
	form = LibroForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('libros')
	return render(request, 'libros/crear.html', {'form': form})


def editar(request):
	return render(request, 'libros/editar.html')


def eliminar(request, libro_id):
	l = get_object_or_404(libro, id=libro_id)
	l.delete()
	return redirect('libros')


def nosotros(request):
	return render(request, 'libreria/nosotros.html')

def image_view(request, pk):
	obj = get_object_or_404(libro, pk=pk)
	with open(obj.image.path, 'rb') as f:
		return HttpResponse(f.read(), content_type='image/jpg')
