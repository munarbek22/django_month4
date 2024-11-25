from django.views import generic
from . import models, forms, parser_litres
from django.http import HttpResponse

class LitresListView(generic.ListView):
    template_name = 'litres/litres_list.html'
    context_object_name = 'litres'
    model = models.Litres

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class LitresFormView(generic.FormView):
    template_name = 'litres/litres_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('200 OK')
        else:
            return super(LitresFormView, self).post(request, *args, **kwargs)