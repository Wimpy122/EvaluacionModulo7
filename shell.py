from app.models import Producto, Categoria, Etiqueta, DetalleProducto

# 1. Crear Categorías
cats = {
    'Electrónica': None,
    'Hogar y Oficina': None,
    'Deportes': None,
    'Ropa': None
}

print("Creando categorías...")
for nombre in cats:
    c, created = Categoria.objects.get_or_create(nombre=nombre)
    cats[nombre] = c

# 2. Crear Etiquetas
tags = {
    'Oferta': None,
    'Nuevo': None,
    'Importado': None,
    'Frágil': None,
    'Eco-Friendly': None
}

print("Creando etiquetas...")
for nombre in tags:
    t, created = Etiqueta.objects.get_or_create(nombre=nombre)
    tags[nombre] = t

# 3. Datos de Productos
productos_data = [
    {
        'nombre': 'Laptop Gamer Xtreme',
        'desc': 'Portátil de alto rendimiento con tarjeta gráfica dedicada.',
        'precio': 1500.00,
        'cat': 'Electrónica',
        'tags': ['Nuevo', 'Importado', 'Frágil'],
        'peso': 2.5,
        'dim': '35x25x2 cm'
    },
    {
        'nombre': 'Silla Ergonómica Pro',
        'desc': 'Silla de oficina con soporte lumbar ajustable.',
        'precio': 250.00,
        'cat': 'Hogar y Oficina',
        'tags': ['Oferta'],
        'peso': 15.0,
        'dim': '60x60x110 cm'
    },
    {
        'nombre': 'Smart TV 4K 55"',
        'desc': 'Televisión inteligente con resolución Ultra HD.',
        'precio': 450.00,
        'cat': 'Electrónica',
        'tags': ['Oferta', 'Frágil'],
        'peso': 12.0,
        'dim': '123x71x8 cm'
    },
    {
        'nombre': 'Botella Térmica Eco',
        'desc': 'Botella de acero inoxidable reutilizable.',
        'precio': 25.50,
        'cat': 'Deportes',
        'tags': ['Eco-Friendly', 'Nuevo'],
        'peso': 0.3,
        'dim': '8x8x25 cm'
    },
    {
        'nombre': 'Kit de Pesas 20kg',
        'desc': 'Juego de mancuernas ajustables para entrenamiento en casa.',
        'precio': 85.00,
        'cat': 'Deportes',
        'tags': ['Importado'],
        'peso': 20.0,
        'dim': '40x20x20 cm'
    }
]

print("Creando productos...")
for p_data in productos_data:
    # Crear producto
    prod = Producto.objects.create(
        nombre=p_data['nombre'],
        descripcion=p_data['desc'],
        precio=p_data['precio'],
        categoria=cats[p_data['cat']]
    )
    
    # Asignar etiquetas (Muchos a Muchos)
    for tag_name in p_data['tags']:
        prod.etiquetas.add(tags[tag_name])
    
    # Crear detalle (Uno a Uno)
    DetalleProducto.objects.create(
        producto=prod,
        peso_kg=p_data['peso'],
        dimensiones=p_data['dim']
    )
    print(f" -> Creado: {prod.nombre}")

print("¡Carga completada exitosamente!")