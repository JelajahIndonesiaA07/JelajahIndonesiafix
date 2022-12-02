from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from tempat_wisata.models import tempat_wisata_Item
from django.views.decorators.csrf import requires_csrf_token
from tempat_wisata.forms import WisataForm
from django.views.decorators.csrf import csrf_protect

@login_required(login_url='/tempat_wisata/login/')
def show_tempat_wisata(request):
    user = request.user
    data_tempat_wisata = tempat_wisata_Item.objects.filter(user=user)
    form = WisataForm(request.POST)
    context = {
    'list_data': data_tempat_wisata,
    'form': form,
    }
    return render(request, "tempat_wisata.html", context)

def get_tempat_wisata(request):
    user = request.user
    data_tempat_wisata = serializers.serialize("json", tempat_wisata_Item.objects.filter(user=user))
    return HttpResponse(data_tempat_wisata, content_type="application/json")

@csrf_protect
def add_tempat_wisata(request):
    if request.method == "POST":
        form = WisataForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect(reverse("tempat_wisata:show_tempat_wisata"))
            return response
    else:
        form = WisataForm()

    context = {'form':form}
    return render(request, 'tempat_wisata.html', context)

requires_csrf_token
def delete_tempat_wisata(request, id):
    task = tempat_wisata_Item.objects.get(id=id)
    task.delete()
    return show_tempat_wisata(request)