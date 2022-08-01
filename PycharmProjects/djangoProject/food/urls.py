from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.get, name = 'get'),
    path('<int:name_id>/', views.detail, name = 'detail'),

]