from django.shortcuts import render
from django.http import HttpResponse


def m1(request, *args, **kwargs):
    return render(request, 'modules/modul_01.html', {})


def m2(request, *args, **kwargs):
    return render(request, 'modules/modul_02.html', {})


def m3(request, *args, **kwargs):
    return render(request, 'modules/modul_03.html', {})


def m4(request, *args, **kwargs):
    return render(request, 'modules/modul_04.html', {})


def m5(request, *args, **kwargs):
    return render(request, 'modules/modul_05.html', {})


def main(request, *args, **kwargs):
    return render(request, 'modules/main.html', {})
