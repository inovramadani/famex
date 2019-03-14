from rest_framework import serializers
from .models import User, Expense, Income, Balance

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Expense
		fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Income
		fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Balance
		fields = '__all__'