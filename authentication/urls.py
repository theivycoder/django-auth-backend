from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView, HelloWorldView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # path('user/register/', CustomUserCreate.as_view(),
    #      name='create_user'),
    path('login/', ObtainTokenPairWithColorView.as_view(),
         name='token_create'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('testview/', HelloWorldView.as_view(),
         name='hello_world'),
    path(r'', include(router.urls)),
]



