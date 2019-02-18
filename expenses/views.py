import json

from django.shortcuts import render
from django.core import serializers

from .models import User


# Create your views here.
def index(request, _id):
	user = User.objects.filter(_id=_id)
	context = {
		'user': serializers.serialize('json', user),
	}
	return render(request, 'expenses/index.html', context)
