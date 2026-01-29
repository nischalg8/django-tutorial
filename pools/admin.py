from django.contrib import admin
from .models import Questions, Choice
# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2  
class QuestionAdmin(admin.ModelAdmin):
     inlines = [ChoiceInLine]
     
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)