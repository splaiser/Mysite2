from django.shortcuts import render


def pricelist(request):
    return render(request, 'main/pricelist.html')




