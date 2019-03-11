from django.urls import path

from . import views

app_name = 'expense'
urlpatterns = [
	# ex: /expense/123
  path('<int:user_id>', views.index, name='index'),
]