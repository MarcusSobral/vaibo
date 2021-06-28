from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

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


# Forms

class UsuarioCreate(CreateView):
    model = Usuarios
    fields = ['name', 'birthdate', 'email', 'country']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')



    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     context['produtos'] = Produtos.objects.all()
    #     paginator = Paginator(context['produtos'], 10)
    #     page = paginator.get_page(1)
    #     return context

# from .models import Smartphone


# class IndexView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context['smartphones'] = Smartphone.objects.all()
#         return context
