from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
def home_view(request, *arg, **kwargs):
    page_all = PageVisit.objects.all()
    page_count = page_all.count()
    context = {'my_name':'Richik','page_count':page_count}
    PageVisit.objects.create()
    return render(request,'index.html',context)