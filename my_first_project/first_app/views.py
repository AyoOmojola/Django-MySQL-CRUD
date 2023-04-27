from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from first_app import models

# def index_test(request):
#     # return HttpResponse('Hello World this is function based view')
#     return render(request,'template',context={})

# class IndexView(View):
#     def get(self, request):
#         return HttpResponse('Hello World this is class based view')

# class IndexView(TemplateView):
#     template_name = 'first_app/index.html'

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs) ## super() means getting from the database
#         context['sample_text1'] = 'sample text 1'
#         context['sample_text2'] = 'sample text 2'
#         return context

class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/index.html'

class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'first_app/musician_details.html'

class AddMusician(CreateView):
    fields = ('first_name','last_name','instrument')
    model = models.Musician
    template_name = 'first_app/musician_form.html'

class UpdateMusician(UpdateView):
    fields = ('first_name','last_name','instrument')
    model = models.Musician
    ### Forms and a Template are magically created when using *UpdateView*, but that which the form displays is modified in the template of the *CreateView*

class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('first_app:index')
    template_name = 'first_app/delete_musician.html'
