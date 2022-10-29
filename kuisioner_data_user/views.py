from django import forms
from django.shortcuts import render
from .forms import kuisioner
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    form = kuisioner(request.POST)

    data = {}

    if (request.is_ajax()):
        if (form.is_valid()):
            form.save()
            data['nama'] = form.cleaned_data.get('nama')
            data['status'] = "ok"
            print("okoklh")
            return JsonResponse(data)

    context = {
        'form': form,
    }

    return render(request, 'index_quiz.html', context)


# Create your views here.
