from django.urls import path, include
from .views import HomeView , BookDetailsView, CreateNewView , BookUpdateView, BookDeleteView
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('<int:pk>/',BookDetailsView.as_view(),name='details'),
    path('new/',CreateNewView.as_view(),name='create'),
    path('<int:pk>/update/',BookUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',BookDeleteView.as_view(),name='delete')
]