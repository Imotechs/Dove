from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dove/index.html')

def about(request):
    return render(request, 'dove/about.html', {'title':'AboutPage'})