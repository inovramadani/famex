from django.urls import path

from . import views

app_name = 'income'
urlpatterns = [
	# ex: /income/123
  path('<int:user_id>', views.index, name='index'),
]