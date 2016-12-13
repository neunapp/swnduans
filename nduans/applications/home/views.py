# django
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    '''
    vista para la pagina de inicio
    '''
    template_name = 'home/home2.html'
