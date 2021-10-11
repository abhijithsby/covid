from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from covid.forms import MovieForm
from covid.models import Movie


def demo(request):
    return render(request,"index.html")

def add_movie(request):
    submitted = False
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add?submitted=True')
    else:
        form=MovieForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'add.html',{'form':form,'submitted':submitted})