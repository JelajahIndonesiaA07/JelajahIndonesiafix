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
# Create your views here.
def ShowActivity(request):
    context = {}
    return render(request, "activity.html",context)

def ShowActivityForms(request):
    # forms_item = Task.objects.filter(user= request.user)
    forms_item = Task.objects.all()
    context = {}
    return render(request, "forms.html",context)

def AddActivity(request):
    if request.method == "POST":
        title = request.POST.get("title")
        print(title)
        description = request.POST.get("description")
        item = Task.objects.create(title = title, description = description, user = request.user)
        item.save()
        JsonResponse({"instance": "Proyek Dibuat"}, status=200)
    return redirect("activity:ShowActivityForms")

def show_json(request):
    # data = Task.objects.filter(user= request.user)
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")