from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from django.urls import path
from inventario.API.vistas import RegisterView

urlpatterns = [
    # Login - obtener tokens (access y refresh)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Refrescar token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Logout - invalidar token
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    # Registro
    path('register/',RegisterView.as_view(), name= 'register')
]
