from django.shortcuts import render,redirect
from .forms import UserForm
from .models import user
from .models import UserActivity

# Create your views here.
def user_list(request):
    context = {'user_list':user.objects.all()}
    return render(request,"userReg/user_list.html",context)

def user_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form = UserForm()
        else:
            user1=user.objects.get(pk=id)
            form=UserForm(instance=user1)
        return render(request,"userReg/user_form.html",{'form':form})
    else:
        if id==0:
            form=UserForm(request.POST)
        else:
            user1=user.objects.get(pk=id)
            form=UserForm(request.POST,instance =user1)
        if form.is_valid():
            form.save()
        return redirect('/user/list')
    
def user_delete(request,id):
    user1=user.objects.get(pk=id)
    user1.delete()
    return redirect('/user/list')

def activity_list(request):
    activities = {'activity_list':UserActivity.objects.all()}
    return render(request,"userReg/activity_list.html",activities)