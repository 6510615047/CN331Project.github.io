from django.urls import path
from folWordSel import views

urlpatterns = [
    path('',views.folder_view,name='folder'),
    path('word/',views.word_view,name='word'),
    path('selectGame/',views.select_game_view,name='select_game'),
]
