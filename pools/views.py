from django.shortcuts import render


def index(request):
    return render(request, 'pools/home.html')

# def about(request):
#     return HttpResponse("This is the about page")

# def contact(request):
#     return HttpResponse("This is contact page");

