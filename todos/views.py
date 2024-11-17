from django.shortcuts import render
from django.urls import reverse_lazy #impotado para retornar a pagina depois de ser efetuado a requisição
'''Abaixo segue os dados feitos para criar o CRUD, listview para mostar, create para criar, update para atualizar
delete para apagar'''
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import User #importa o arquivo models dentro do todos, para ser usado a class criada nele
# Create your views here.


'''Criar somente o model = User(classe criada no models.py)'''
class UserListView(ListView): 
    model = User

'''Criar  o model = User(classe criada no models.py)
depois o fields q é o formulário do seu html, onde vc vai chamar no user_form.html pelo 
{% csrf_token %} e depois o {{form.as_p}}'''

class UserCreateView(CreateView):
    model = User
    fields = ['nome', 'idade']
    success_url = reverse_lazy('user_list')

'''Similar ao create, muda q dessa vez vc está atualizando, 
lembrando q n precisa criar um html para ele, mas precisa ter um name diferente no urls.py'''
class UserUpdateView(UpdateView):
    model = User
    fields = ['nome', 'idade']
    success_url = reverse_lazy('user_list')

'''Criar  o model = User(classe criada no models.py)
depois o fields q é o formulário do seu html, onde vc vai chamar no user_confirm_delete.html pelo 
{% csrf_token %} e so, não usar o {{form.as_p}}'''
class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')