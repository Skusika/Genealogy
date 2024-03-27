from django.urls import path, include
from rest_framework import routers

from .views import *

# app_name = 'study'

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'section', SectionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
