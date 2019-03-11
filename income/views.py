from django.shortcuts import render, get_object_or_404
from django.core import serializers

from home.models import User, Income, Balance

# Create your views here.
def index(request, user_id):
	get_object_or_404(User, pk=user_id)
	user = User.objects.filter(user_id=user_id)
	incomes = Income.objects.filter(user_id=user_id)
	balance = Balance.objects.filter(user_id=user_id)
	currency = balance[0].currency
	context = {
		'user': serializers.serialize('json', user),
		'incomes': serializers.serialize('json', incomes),
		'currency': currency,
	}
	return render(request, 'income/index.html', context)