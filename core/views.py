from django.views.generic import TemplateView

from .models import Produtos


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtos'] = Produtos.objects.all()
        return context

# from .models import Smartphone


# class IndexView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context['smartphones'] = Smartphone.objects.all()
#         return context
