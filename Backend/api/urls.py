from django.urls import path
from .views import *
urlpatterns = [
    path('api/notes', NotesList.as_view()),
    path('api/notes/<int:pk>/', NotesDetail.as_view()),  
    path('api/notes/<int:pk>/share', fnShareNotes, name='fnshare'),  
    path('api/search/', fnSearchNote, name='fnsearch'),  
]