from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    # path("about/", views.about, name='about'),
    # path("contact/", views.contact, name='contact')
    path('<int:question_id>/', views.question_detail,name='question_detail'),
    path("question/", views.question_choice_view, name='questions_choice' )
]