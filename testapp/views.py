from django.shortcuts import render
from testapp.models import student
# Create your views here.
def empdata(request):
    emp_list=student.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/index.html',context=my_dict)