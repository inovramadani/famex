from django.shortcuts import render, get_object_or_404
from django.core import serializers

from home.models import User, Expense, Balance

# Create your views here.
def index(request, user_id):
	get_object_or_404(User, pk=user_id)
	user = User.objects.filter(user_id=user_id)
	expenses = Expense.objects.filter(user_id=user_id)
	balance = Balance.objects.filter(user_id=user_id)
	currency = balance[0].currency
	print(type(currency))
	context = {
		'user': serializers.serialize('json', user),
		'expenses': serializers.serialize('json', expenses),
		'currency': currency,
	}
	return render(request, 'expense/index.html', context)