from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg, Count
from .models import Producto, Categoria, Etiqueta, DetalleProducto
from .forms import ProductoForm, DetalleProductoForm, CategoriaForm, EtiquetaForm

# Create your views here.

def index(request):
    total_productos = Producto.objects.count()
    productos_vip = Producto.objects.filter(precio__gt=1000)
    productos_sin_cat_basica = Producto.objects.exclude(categoria__nombre='Básicos')
    stats_categorias = Categoria.objects.annotate(num_productos=Count('productos'))
    sql_query = Producto.objects.raw('SELECT id, nombre, precio FROM app_producto ORDER BY precio DESC LIMIT 5')

    context = {
        'total_productos': total_productos,
        'productos_vip': productos_vip,
        'stats_categorias': stats_categorias,
        'sql_raw_ejemplo': sql_query,
    }
    return render(request, 'index.html', context)

def lista_productos(request):
    query = request.GET.get('q')
    categoria_id = request.GET.get('categoria')

    productos = Producto.objects.all().select_related('categoria', 'detalle').prefetch_related('etiquetas')

    if query:
        productos = productos.filter(nombre__icontains=query)
    
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    categorias = Categoria.objects.all()
    return render(request, 'lista.html', {'productos': productos, 'categorias': categorias})

def crear_producto(request):
    if request.method == 'POST':
        form_prod = ProductoForm(request.POST)
        form_det = DetalleProductoForm(request.POST)
        if form_prod.is_valid() and form_det.is_valid():
            producto = form_prod.save()
            detalle = form_det.save(commit=False)
            detalle.producto = producto 
            detalle.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('lista_productos')
    else:
        form_prod = ProductoForm()
        form_det = DetalleProductoForm()
    
    return render(request, 'crear.html', {'form_prod': form_prod, 'form_det': form_det, 'titulo': 'Crear Producto'})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'detalle.html', {'producto': producto})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    detalle_instancia = getattr(producto, 'detalle', None)

    if request.method == 'POST':
        form_prod = ProductoForm(request.POST, instance=producto)
        form_det = DetalleProductoForm(request.POST, instance=detalle_instancia)
        
        if form_prod.is_valid() and form_det.is_valid():
            prod = form_prod.save()
            det = form_det.save(commit=False)
            det.producto = prod
            det.save()
            messages.success(request, 'Producto actualizado.')
            return redirect('lista_productos')
    else:
        form_prod = ProductoForm(instance=producto)
        form_det = DetalleProductoForm(instance=detalle_instancia)

    return render(request, 'crear.html', {'form_prod': form_prod, 'form_det': form_det, 'titulo': 'Editar Producto'})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado.')
        return redirect('lista_productos')
    return render(request, 'eliminar.html', {'object': producto, 'tipo': 'Producto'})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/formulario.html', {'form': form, 'titulo': 'Editar Categoría'})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'eliminar.html', {'object': categoria, 'tipo': 'Categoría'})

def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'etiquetas/lista.html', {'etiquetas': etiquetas})

def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    return render(request, 'etiquetas/formulario.html', {'form': form, 'titulo': 'Crear Etiqueta'})

def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, pk=id)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'etiquetas/formulario.html', {'form': form, 'titulo': 'Editar Etiqueta'})

def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, pk=id)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')
    return render(request, 'eliminar.html', {'object': etiqueta, 'tipo': 'Etiqueta'})