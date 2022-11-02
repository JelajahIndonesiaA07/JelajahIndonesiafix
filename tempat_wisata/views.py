from django.http import response, JsonResponse
from django.shortcuts import render
from datetime import datetime, date
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from tempat_wisata.forms import WisataForm
from .models import wisata, filter
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.urls import reverse

def index(request):
    form = WisataForm()

    if (request.method == "GET" and form.is_valid):       
        if 'reset_button' in request.GET:
            data = wisata.objects.all()
            response = {'data':data}
            form.save()
            return render(request, "tempat_wisata.html", response)

    data = wisata.objects.all()
    response = {'data':data}
    return render(request, "tempat_wisata.html", response)

@csrf_exempt
def allData(request):
    data = serializers.serialize('json', wisata.objects.all())
    return JsonResponse(data, content_type="application/json", safe=False)
