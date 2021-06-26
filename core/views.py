from django.views.generic import TemplateView
from django.views.generic.list import ListView

# from django.core.paginator import Paginator

from .models import Produtos


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
