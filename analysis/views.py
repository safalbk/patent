from django.shortcuts import render
from .models import Profile,CompanyDataTable,PatentDataTable,InventorsDataTable
# Create your views here.

def analysis(request):
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

    return render(request,'analysis.html',context)
def cv(request):
    return render(request,'cv.html')
def index(request):
    # q = CompanyDataTable.objects.all()
    # print(q)
    return render(request,'index.html')
