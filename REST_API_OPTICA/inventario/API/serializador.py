from rest_framework import serializers
from django.contrib.auth.models import User
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


#! Manejo del login
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Para que la contraseña no sea incluida en las respuestas
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])  # Hashea la contraseña
        user.save()
        return user

    def update(self, instance, validated_data):
        # Extraer la contraseña si está presente
        password = validated_data.pop('password', None)
        # Actualizar los demás campos
        user = super().update(instance, validated_data)
        # Asignar y hashear la contraseña si se proporciona
        if password:
            user.set_password(password)
            user.save()
        return user