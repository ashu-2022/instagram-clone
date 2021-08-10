from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from authentication.forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout,get_user_model
# from user.models import User
from django.contrib.auth.views import ( 
    PasswordResetView,
     PasswordResetDoneView, 
     PasswordResetConfirmView,
     PasswordResetCompleteView,
     PasswordChangeView,
     PasswordChangeDoneView
      )
# Create your views here.

# def home(request):
#     return HttpResponse("home")
User=get_user_model()
#class based views
class SignUpView(View):
    template_name = "authentication/signup.html"
    form_class=UserForm
    

    # for get method
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

    # for post method
    def post(self,request,*args,**kwargs):
        form =self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_view')
        context = {'form' : form}
        return render(request,self.template_name,context)


class SignInView(View):
    template_name = "authentication/signin.html"
    # for get method
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home_feed_view')
        return render(request,self.template_name)

    # for post method
    def post(self,request,*args,**kwargs):
        email_username=request.POST.get('email_username')
        password=request.POST.get('password')
        try:
            user_obj = User.objects.get(username=email_username)
            email=user_obj.email
        except Exception as e:
            email=email_username

        user=authenticate(request,email=email,password=password)
        if user is None:
            messages.error(request,'Invalid Login')
            return render(request,self.template_name)
        login(request,user)
        messages.success(request,f'welcome back {user.username}')
        return redirect('home_feed_view')


class SignOutView(View):
    def post(self, request,*args, **kwargs):
        logout(request)
        return redirect('signin_view')
 
    
class PRView(PasswordResetView):
    email_template_name='authentication/password_reset_email.html'
    template_name = "authentication/password_reset.html"

class PRDone(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'


class PRConfirm(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'

class PRComplete(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'

# since we used directly in urls 
# that's why here both below views not working

class PWDChangeView(PasswordChangeView):
    template_name = 'authentication/password_change.html'
    success_url =reverse_lazy('password_change_done_view')  # dynamically get urls


class PWDChangeDoneView(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'

"""
function based views

def signup_view(request):
    if request.method=='POST':
        #code
    if request.method=='GET':
        #code

"""