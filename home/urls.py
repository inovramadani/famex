from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
	# ex: /expenses/123
  path('<int:user_id>', views.index, name='index'),
]