from django.shortcuts import render
from .models import Questions
from django.shortcuts import get_object_or_404
from .forms import ChoiceForm 

def index(request):
    questions = Questions.objects.all() 
    return render(request, 'pools/home.html', {'questions': questions}) 

def question_detail(request, question_id):
    
    query = get_object_or_404(Questions, pk=question_id)
    return render(request, 'pools/question_details.html', {'questions': query})

def question_choice_view(request):
    selected_choice = None  
    questions = None
    
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            selected_choice = form.cleaned_data['choice_option']
            questions  = selected_choice.question
    else:
        form = ChoiceForm()
        
    return render(request,
                  'pools/question_choice.html', 
                  {   'form': form,
                      'question': questions,
                      'selected_choice': selected_choice, })