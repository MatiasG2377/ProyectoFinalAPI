from rest_framework import viewsets
from inventario.models import Categoria, Proveedor, Producto, ProductoProveedor, Cliente, Venta, ArticuloVenta, MovimientoInventario, Lote
from inventario.API.serializador import categoriaSerializer, productoSerializer, proveedorSerializer, productoProveedorSerializer, clienteSerializer, ventaSerializer, articuloVentaSerializer, movimientoInventarioSerializer, loteSerializer

class categoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = categoriaSerializer

class productoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = productoSerializer

class proveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = proveedorSerializer

class productoProveedorViewSet(viewsets.ModelViewSet):
    queryset = ProductoProveedor.objects.all()
    serializer_class = productoProveedorSerializer

class clienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = clienteSerializer

class ventaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = ventaSerializer

class articuloVentaViewSet(viewsets.ModelViewSet):
    queryset = ArticuloVenta.objects.all()
    serializer_class = articuloVentaSerializer

class movimientoInventarioViewSet(viewsets.ModelViewSet):
    queryset = MovimientoInventario.objects.all()
    serializer_class = movimientoInventarioSerializer

class loteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = loteSerializer