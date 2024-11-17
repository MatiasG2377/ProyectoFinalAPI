from rest_framework import serializers
from inventario.models import Categoria, Proveedor, Producto, ProductoProveedor, Cliente, Venta, ArticuloVenta, MovimientoInventario, Lote

class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class proveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class productoProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoProveedor
        fields = '__all__'

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ventaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class articuloVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticuloVenta
        fields = '__all__'

class movimientoInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoInventario
        fields = '__all__'

class loteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'