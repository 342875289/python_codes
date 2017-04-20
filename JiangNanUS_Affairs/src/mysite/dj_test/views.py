from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse,HttpResponseNotFound
import datetime
from django.shortcuts import render
from .forms import NameForm,PersonForm
from .models import Person,Name
from django.views import View
# Create your views here.
class NameFormView(View):
    form_class = NameForm
    template_name = 'dj_test/name.html'
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponse('<html><body>success</body></html>')

        return render(request, self.template_name, {'form': form})


def test_index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            Name.objects.create( name=form.cleaned_data['your_name'] ,age=form.cleaned_data['your_age']  )
            # redirect to a new URL:
            html = "<html><body><p>Hello , %s.</p><p>data bas been saved.</p></body></html>" % form.cleaned_data['your_name']
            return HttpResponse(html)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'dj_test/name.html', {'form': form})

def get_person(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            Person.objects.create( first_name=form.cleaned_data['first_name'] ,last_name=form.cleaned_data['last_name']  )
            # redirect to a new URL:
            html = "<html><body><p>Hello , %s.</p><p>data bas been saved.</p></body></html>" % form.cleaned_data['first_name']
            return HttpResponse(html)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()
    return render(request, 'dj_test/person.html', {'form': form})