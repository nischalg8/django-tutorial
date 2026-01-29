from django.shortcuts import render
from .models import Questions, Choice
from django.shortcuts import get_object_or_404


def index(request):
    questions = Questions.objects.all() 
    return render(request, 'pools/home.html', {'questions': questions}) 

def question_detail(request, question_id):
    
    query = get_object_or_404(Questions, pk=question_id)
    return render(request, 'pools/question_details.html', {'questions': query})
