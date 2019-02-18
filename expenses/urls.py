from django.urls import path

from . import views

app_name = 'expenses'
urlpatterns = [
	# ex: /expenses/123
  path('<int:_id>', views.index, name='index'),
]