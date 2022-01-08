from django.shortcuts import render
from .models import Resume
from .forms import ResumeForm
from django.views import View
 
# Create your views here.

# def index(request):
#     form = ResumeForm()
#     return render(request, 'myapp/index.html', {'form':form})

class Index(View):
    def get(self, request):
        form = ResumeForm()
        return render(request, 'myapp/index.html', {'form':form})