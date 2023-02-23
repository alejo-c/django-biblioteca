from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import libro
from .forms import LibroForm


# Create your views here.
@login_required
def inicio(request):
    return render(request, "libros/index.html")


@login_required
def libros(request):
    libros = libro.objects.all()
    return render(request, "libros/libros.html", {"libros": libros})


@login_required
def crear(request):
    form = LibroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("libros")
    return render(request, "libros/crear.html", {"form": form})


@login_required
def editar(request, libro_id):
    libro_editar = libro.objects.get(id=libro_id)
    form = LibroForm(request.POST or None, request.FILES or None, instance=libro_editar)
    if form.is_valid() and request.POST:
        form.save()
        return redirect("libros")
    return render(request, "libros/editar.html", {"form": form})


@login_required
def borrar(request, libro_id):
    libro_borrar = libro.objects.get(id=libro_id)
    libro_borrar.delete()
    return redirect("libros")


@login_required
def nosotros(request):
    return render(request, "libreria/nosotros.html")

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')