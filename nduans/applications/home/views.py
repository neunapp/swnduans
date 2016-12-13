# django
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    '''
    vista para la pagina de inicio
    '''
    template_name = 'tema/theme/detail.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['portada'] = '5 amigos'
        return context
