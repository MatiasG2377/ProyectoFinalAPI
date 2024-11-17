from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

#! Opciones para los estados de los productos
ESTADO_PRODUCTO_CHOICES = [
    ('Disponible', 'Disponible'),
    ('Reservado', 'Reservado'),
    ('Agotado', 'Agotado'),
]

#! Opciones para los estados de las ventas
ESTADO_VENTA_CHOICES = [
    ('P', 'Pendiente'),
    ('C', 'Cancelado'),
    ('F', 'Finalizado'),
]

#! Los ID de cada tabla se generan de manera automática en la BD
# Categoría de productos
class Categoria(models.Model):
    nombre_categoria = models.TextField(null=False) # Nombre de la categoría
    descripcion_categoria = models.TextField(blank=True, null=True) # Descripción de la categoría
    activo_categoria = models.BooleanField(default=True) # Este campo sirve para eliminación lógica de categorías
    relevancia_categoria = models.IntegerField(default=0)  # Servirá para establecer un orden dentro de los datos 
    fecha_creacion_categoria = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    actualizacion_categoria = models.DateTimeField(auto_now=True)      # Fecha de última actualización

    def __str__(self):
        return self.nombre_categoria


# Proveedores
class Proveedor(models.Model):
    nombre_proveedor = models.TextField(null=False) # Nombre de la empresa proveedora
    informacion_proveedor = models.TextField(blank=True, null=True) # Información del proveedor
    correo_proveedor = models.EmailField(unique=True, blank=True, null=True) # Correo electrónico del proveedor
    telefono_proveedor = models.TextField(blank=True, null=True) # Número telefónico del proveedor
    direccion_proveedor = models.TextField(blank=True, null=True) # Dirección del proveedor

    def __str__(self):
        return self.nombre_proveedor


# Productos
class Producto(models.Model):
    nombre_producto = models.TextField(null=False) # NOmbre del producto
    categoria_producto = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True) # ForeignKey de categoria 
    pvp_producto = models.DecimalField(max_digits=10, decimal_places=2, null=False) # Precio del producto
    costo_producto = models.DecimalField(max_digits=10, decimal_places=2) # Costo del la adquisición del producto
    cantidad_producto = models.IntegerField(null=False) # cantidad disponible
    minimo_producto = models.IntegerField(default=0) # Stock mínimo
    maximo_producto = models.IntegerField(default=100) # Stock máximo
    fecha_ingreso_producto = models.DateTimeField(auto_now_add=True) # Fecha de ingreso del producto
    estado_producto = models.CharField(max_length=20, choices=ESTADO_PRODUCTO_CHOICES, default='Disponible') # Estado del producto en el inventario
    descripcion_producto = models.TextField(blank=True, null=True) # Descripción del producto
    marca_producto = models.TextField(blank=True, null=True) # Marca del producto
    proveedores_producto = models.ManyToManyField(Proveedor, through='ProductoProveedor') # Define relación muchos a muchos entre proveedor y producto a través de la tabla "ProductoProveedor"
    ultima_venta_producto = models.DateTimeField(blank=True, null=True) #Ultima venta del producto

def clean(self):
    if self.minimo_producto > self.maximo_producto:
        raise ValidationError("El stock mínimo no puede ser mayor que el stock máximo.")
    if self.cantidad_producto < 0:
        raise ValidationError("La cantidad en stock no puede ser negativa.")

    def __str__(self):
        return f"{self.nombre_producto}"


# Relación entre Productos y Proveedores
class ProductoProveedor(models.Model):
    producto_productoProveedor  = models.ForeignKey(Producto, on_delete=models.CASCADE) # ForeignKey del Producto
    proveedor_productoProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE) # ForeignKey del proveedor
    costo_productoProveedor = models.DecimalField(max_digits=10, decimal_places=2) # Registrar el costo de adquisición del producto
    tiempo_entrega_productoProveedor = models.IntegerField(help_text="Días para entrega", blank=True, null=True) # Registrar el tiempo en dpias de entrega

    def __str__(self):
        return f"{self.proveedor_productoProveedor.nombre_proveedor} - {self.porducto_productoProveedor.nombre_producto}"


# Clientes
class Cliente(models.Model):
    ci_cliente = models.TextField(null=False) # Identificación del cliente
    nombre_cliente = models.TextField(null=False) # Nombre del cliente
    informacion_cliente = models.TextField(blank=True, null=True) # Información del cliente
    correo_cliente = models.EmailField(unique=True, blank=True, null=True) # Correo del cliente
    telefono_cliente = models.TextField(blank=True, null=True) # Teléfono del cliente
    direccion_cliente = models.TextField(blank=True, null=True) # Dirección del cliente

    def __str__(self):
        return self.nombre_cliente


# Ventas
class Venta(models.Model):
    cliente_venta = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True) # ForeignKey del cliente
    fecha_venta = models.DateTimeField(auto_now_add=True) # Fecha de la venta
    total_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # Total de la venta
    estado_venta = models.CharField(max_length=1, choices=ESTADO_VENTA_CHOICES, default='P') # Estado de venta
    metodo_venta = models.CharField(max_length=255, blank=True, null=True)  # Efectivo, tarjeta, etc.

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_venta}"


# Artículos vendidos en una venta
class ArticuloVenta(models.Model):
    venta_articuloVenta = models.ForeignKey(Venta, on_delete=models.CASCADE) # ForeignKey de la venta
    producto_articuloVenta = models.ForeignKey(Producto, on_delete=models.CASCADE) # ForeignKey del producto
    cantidad_articuloVenta = models.IntegerField(null=False) #Cnatidad de producto en la venta
    pvp_articuloVenta = models.DecimalField(max_digits=10, decimal_places=2, null=False) # Precio 
    descuento_articuloVenta = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) # Descuento del producto

    def __str__(self):
        return f"Artículo {self.producto_articuloVenta.nombre_producto} en Venta #{self.venta_articuloVenta.id}"


# Movimientos de inventario (entradas/salidas)
class MovimientoInventario(models.Model):
    producto_movimientoInventario = models.ForeignKey(Producto, on_delete=models.CASCADE) # ForeignKey del producto
    tipo_movimientoInventario = models.CharField(max_length=10, choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')]) # Tipo de movimiento en el inventario
    cantidad_movimientoInventario = models.IntegerField(null=False) # Cantidad de productos movidos
    fecha_movimientoInventario = models.DateTimeField(auto_now_add=True) # Fecha del movimiento del inventario
    motivo_movimientoInventario = models.TextField(blank=True, null=True)  # Ej: Venta, ajuste, devolución

    def __str__(self):
        return f"{self.tipo_movimientoInventario} - {self.producto_movimientoInventario.nombre_producto} ({self.cantidad_movimientoInventario})"


# Lotes de productos
class Lote(models.Model):
    producto_lote = models.ForeignKey(Producto, on_delete=models.CASCADE) # ForeignKey del producto
    cantidad_lote = models.IntegerField() # Cantidad de unidades en el lote
    fecha_ingreso_lote = models.DateTimeField(auto_now_add=True) # Fecha de ingreso en el lote
    fecha_caducidad_lote = models.DateField(blank=True, null=True) # Fecha de caducidad en productos que aplique

    def __str__(self):
        return f"Lote de {self.producto_lote.nombre_producto} ({self.cantidad_lote} unidades)"
