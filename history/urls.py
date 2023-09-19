from django.urls import path, include
from rest_framework import routers
from .views.class_views import PostViewSet, PostDetail

router = routers.DefaultRouter()

router.register(r'', viewset=PostViewSet, basename="post")

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', view=PostDetail.as_view(), name="detail")
]