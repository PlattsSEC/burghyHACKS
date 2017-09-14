from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic import View
#from .forms import userForm
from burghyhacks.settings import BASE_DIR
from burghyHACKS.forms import userForm
import os


# Create your views here.

def index(request):
    temp = loader.get_template("index.html")
    return HttpResponse(temp.render())
    
class userFormView(View):
    #form_class = userForm
    template_name = os.path.join(BASE_DIR,"burghyHACKS/templates/user_form.html")
    fields = ['first_name','last_name','email','password']
    
    def get(self, request):
        #form = self.form_class(None)
        form = userForm(request.GET)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request):
        #form = self.form_class(request.POST)
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        else:
            return HttpResponse('form invalid')
