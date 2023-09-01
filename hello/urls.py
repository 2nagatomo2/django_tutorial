from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name='next'),
    path('<int:id>/<nickname>/', views.id_name),
    path('my_name_is_<nickname>.I_am_<int:age>_years_old.', views.name_age)
]
