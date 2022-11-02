from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from activity.models import Task
from .forms import CreateForm
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.
def ShowActivityJakarta(request):
    context = {}
    return render(request, "activity.html",context)

def ShowActivityBali(request):
    context = {}
    return render(request, "bali.html",context)

def ShowActivityJogja(request):
    context = {}
    return render(request, "jogja.html",context)

def ShowActivityJabar(request):
    context = {}
    return render(request, "jabar.html",context)

def ShowActivityJateng(request):
    context = {}
    return render(request, "jateng.html",context)

def ShowActivityJatim(request):
    context = {}
    return render(request, "jatim.html",context)


def ShowActivityForms(request):
    # forms_item = Task.objects.filter(user= request.user)
    forms_item = Task.objects.all()
    form = CreateForm(request.POST)
    context = {
        'list_activity': forms_item,
        'form': form,
    }
    return render(request, "forms.html",context)

requires_csrf_token
def AddActivity(request):
    form = CreateForm(request.POST)
    if request.method == "POST":
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return  ShowActivityForms(request)
    context = {'form': form}
    return render( request, 'forms.html', context)

def show_json(request):
    # data = Task.objects.filter(user= request.user)
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def hapus(request, id):
    data = Task.objects.get(id=id)
    data.delete()
    return  ShowActivityForms(request)