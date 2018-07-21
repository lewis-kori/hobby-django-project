from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from . forms import EditProfileForm
from django.shortcuts import render,redirect
from django.contrib.auth import update_session_auth_hash
# Create your views here.
class IndexView(generic.ListView):
    template_name='eshop/home.html'
    def get_queryset(self):
        pass
#view for displaying the user profile
def profile(request):
    context={'user':request.user}
    return render(request,'eshop/profile.html',context)
#view for editing user profile
def edit_profile(request):
    if request.method=='POST':
        form=EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save(request)
            return redirect('eshop:profile')
        
    else:
        form=EditProfileForm(instance=request.user)
        context={'form':form}
        return render(request,'eshop/edit_profile.html',context)
   #view for changing the user password     
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save(request)
            update_session_auth_hash(request,form.user)
            return redirect('eshop:profile')
        else:
            return redirect('eshop:change_password')
    else:
        form=PasswordChangeForm(user=request.user)
        context={'form':form}
        return render(request,'eshop/edit_password.html',context)
    