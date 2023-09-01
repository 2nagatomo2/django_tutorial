from django.urls import path
from .views import HelloView
from . import views

urlpatterns = [
    path(r'', HelloView.as_view(), name='index'),
    path('<int:id>/<nickname>/', views.id_name),
    path('my_name_is_<nickname>.I_am_<int:age>_years_old.', views.name_age)
]
