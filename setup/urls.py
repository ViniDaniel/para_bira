
from django.contrib import admin
from django.urls import path
'''Abaixo segue da forma como foi criada as classes no views.py'''
from todos.views import (
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserListView.as_view(), name='user_list'),
    path('cadastro', UserCreateView.as_view(), name='user_form'),
    path('editar/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('deletar/<int:pk>/', UserDeleteView.as_view(), name='user_confirm_delete')
]
'''<int:pk> serve para referenciar o id como um inteiro, não pode esquecer de por, se não ele não acha 
o q vc quer editar'''