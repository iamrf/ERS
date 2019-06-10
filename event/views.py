from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from . import models
from . import forms

# Create your views here.


class EventIndexView(generic.ListView):
    template_name = 'event/index.html'
    context_object_name = 'events'

    def get_queryset(self):
        return models.Event.objects.order_by('date')


class EventDetailView(generic.DetailView):
    template_name = 'event/detail.html'
    model = models.Event


def user_register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('completed/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.UserForm()

    return render(request, 'event/register.html', {'form': form})


def completed_register(request):
    return render(request, 'event/completed.html')
