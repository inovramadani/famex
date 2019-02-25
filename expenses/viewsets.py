from rest_framework import viewsets
from .models import User, Expense, Income
from .serializers import UserSerializer, ExpenseSerializer, IncomeSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
	queryset = Expense.objects.all()
	serializer_class = ExpenseSerializer

class IncomeViewSet(viewsets.ModelViewSet):
	queryset = Income.objects.all()
	serializer_class = IncomeSerializer