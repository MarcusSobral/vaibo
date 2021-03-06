from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

# from django.core.paginator import Paginator

from .models import Produtos, Usuarios


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtos'] = Produtos.objects.all()
        return context


class ProdutosIndexView(TemplateView):
    template_name = 'produtos/index.html'


class ProdutosList(ListView):
    model = Produtos
    template_name = "produtos/produto-card2.html"
    paginate_by = 30


class ProdutoDescricao(TemplateView):
    template_name = 'produtos/produto-descricao.html'


# CREATE ############

class UsuarioCreate(CreateView):
    model = Usuarios
    fields = ['name', 'birthdate', 'email', 'country']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


# UPDATE ############

class UsuarioUpdate(UpdateView):
    model = Usuarios
    fields = ['name', 'birthdate', 'email', 'country']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


# DELETE ############
class UsuarioDelete(DeleteView):
    model = Usuarios
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
