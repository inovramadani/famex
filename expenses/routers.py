from rest_framework import routers
# from expenses.viewsets import UserViewSet
from .viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)