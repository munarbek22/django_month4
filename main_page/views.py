from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


# Search button
class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    paginate_by = 5

    def get_queryset(self):
        return models.Library.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context




class BookList_view(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    model = models.Library

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')



# def book_list_view(request):
#     if request.method == 'GET':
#         book_list = models.Library.objects.filter().order_by('-id')
#         context = {'book_list': book_list}
#         return render(request, template_name='book.html', context=context)



class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Library, id=film_id)

# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Library, id=id)
#         context = {'book_id': book_id}
#         return render(request, template_name='book_detail.html', context=context)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Привет, я Мунарбек и я изучаю пайтон')

def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse("имя  питомца - Хатико, фото питомца-<img src = 'https://www.princeton.edu/sites/default/files/styles/1x_full_2x_half_crop/public/images/2022/02/KOA_Nassau_2697x1517.jpg?itok=Bg2K7j7J' >")

def system_time(request):
    current_data = datetime.now()
    if request.method == 'GET':
        return HttpResponse(f'текущее время: {current_data}')