from django import forms
from django.forms.utils import pretty_name
from django.shortcuts import render
from .forms import AssessmentForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    form = AssessmentForm(request.POST)

    data = {}

    if (form.is_valid()):
        form.save()
        data['nama'] = form.cleaned_data.get('nama')
        data['status'] = "ok"
        print("okoklh")
        return JsonResponse(data)

    context = {
        'form': form,
    }

    return render(request, 'pertanyaan_kuisioner.html', context)


def hasil(request):
    return render(request, 'hasil_kuisioner.html')

# Create your views here.
