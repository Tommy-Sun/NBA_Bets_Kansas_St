from django.urls import path

from . import views

urlpatterns = [
    path('new_better', views.new_better, name='new_better'),
    path('<int:id>', views.detail, name='detail'),
    path('test', views.test),
]