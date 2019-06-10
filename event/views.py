from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'ers/index.html'
    context_object_name = 'events'

    def get_queryset(self):
        return models.Event.objects.order_by('-date')


class DetailView(generic.DetailView):
    template_name = 'ers/detail.html'
    model = models.Event
