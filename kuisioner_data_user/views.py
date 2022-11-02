from django.shortcuts import render
from .forms import AssessmentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/mainpage/login/')
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


@login_required(login_url='/mainpage/login/')
def hasil(request):
    return render(request, 'hasil_kuisioner.html')

# Create your views here.
