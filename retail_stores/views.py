from django.http import HttpResponse
from django.shortcuts import render


def load_store(request, retail):

    return render(request, 'retail/store.html');
