from django.urls import path
from .views import HelloView
from . import views

urlpatterns = [
    path(r'', HelloView.as_view(), name='index'),
    path('friend/', views.friend, name='friend'),
    path('friend/record/', views.friend_record, name='friend_record'),
    path('create/', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('find', views.find, name='find'),
    path('<int:id>/<nickname>/', views.id_name),
    path('my_name_is_<nickname>.I_am_<int:age>_years_old.', views.name_age)
]
