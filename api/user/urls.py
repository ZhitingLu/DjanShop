from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.CustomUserViewSet)

urlpatterns = [
    path('logout/<int:id>/', views.signout, name='signout'),
    path('login/', views.signin, name='signin'),
    path('', include(router.urls)),
]

