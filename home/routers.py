from rest_framework import routers
from .viewsets import UserViewSet, ExpenseViewSet, IncomeViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'expense', ExpenseViewSet)
router.register(r'income', IncomeViewSet)