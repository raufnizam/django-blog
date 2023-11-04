from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'allIn/index.html')


# def home(request):
#     return render(request, 'allIn\/home.html')