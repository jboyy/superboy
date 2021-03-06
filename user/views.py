from django.shortcuts import render,HttpResponse,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user import forms
# Create your views here.
def register(request):
    if request.method == 'POST':
     form = forms.UserRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success (request,f'Account created for {username}')
        return redirect('login')
    else:      
     form = forms.UserRegistrationForm()
    return render(request,'register.html',{'form':form})
@login_required
def profile(request): 
    if request.method == 'POST':
      u_form = forms.UserUpdateForm(request.POST, instance=request.user)
      p_form = forms.ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
      if u_form.is_valid and p_form.is_valid:
          u_form.save()
          p_form.save()
          messages.success(request,f"your account has been  updated!")
          return redirect('profile')
    else:
      u_form = forms.UserUpdateForm(request.POST,instance = request.user)
      p_form = forms.ProfileUpdateForm(request.POST,instance = request.user.profile)
      
    context = {
      'u_form':u_form,'p_form':p_form}
    return render(request,"profile.html",context)
    

