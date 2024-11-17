from rest_framework import viewsets
from inventario.models import Categoria, Proveedor, Producto, ProductoProveedor, Cliente, Venta, ArticuloVenta, MovimientoInventario, Lote
from inventario.API.serializador import categoriaSerializer, productoSerializer, proveedorSerializer, productoProveedorSerializer, clienteSerializer, ventaSerializer, articuloVentaSerializer, movimientoInventarioSerializer, loteSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]  # Permite acceso sin autenticación
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)