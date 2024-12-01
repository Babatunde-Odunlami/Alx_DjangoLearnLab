from api.views import BookViewSet
from django.urls import path, include
from rest_framework import routers

#create an instance of a routers.DefaultRouter
router =routers.DefaultRouter()

#register the BookViewSet with the router
router.register(r'books', BookViewSet, basename='book')

urlspatterns = [
        path('api/', include(router.urls)),
        ]
