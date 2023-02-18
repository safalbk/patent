from django.shortcuts import render
from .models import Profile
# Create your views here.

def index(request):
    labels = []
    data = []
    context={
        'labels':labels,
        'data':data
    }
    queryset = Profile.objects.order_by('-age')[:5]
    for person in queryset:
        labels.append(person.name)
        data.append(person.age)

    return render(request,'index.html',context)