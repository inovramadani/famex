from django.shortcuts import render, get_object_or_404
from django.core import serializers

from .models import User, Expense, Balance


# Create your views here.
def index(request, user_id):
	get_object_or_404(User, pk=user_id)
	user = User.objects.filter(user_id=user_id)
	expenses = Expense.objects.filter(user_id=user_id)
	balance = Balance.objects.filter(user_id=user_id)
	context = {
		'user': serializers.serialize('json', user),
		'expenses': serializers.serialize('json', expenses),
		'balance': serializers.serialize('json', balance),
	}
	return render(request, 'home/index.html', context)
