from rest_framework import routers
from .viewsets import UserViewSet, ExpenseViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'expense', ExpenseViewSet)