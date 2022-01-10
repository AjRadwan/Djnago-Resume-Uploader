from django.shortcuts import render, redirect
from .models import Resume
from django.contrib import messages
from .forms import ResumeForm
from django.views import View
 
# Create your views here.

# def index(request):
#     form = ResumeForm()
#     return render(request, 'myapp/index.html', {'form':form})

class Index(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'myapp/index.html', {'candidates':candidates,'form':form})
    
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save();
            messages.success(request, "Your From has been submitted")
            return redirect('myapp/index.html')
            
            
        