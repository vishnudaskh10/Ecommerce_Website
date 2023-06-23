from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product
from django.db.models import Q
def searchresult(request):
    products=None
    query=""
    if request.method=='POST':
        query=request.POST.get('q')
        if query:
            products=product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'search.html',{'query':query,'products':products})