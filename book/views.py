from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView, TemplateView
from django.urls import reverse_lazy

from .models import Book_shelf
# Create your views here.
class HomeView(ListView):
    template_name= 'home.html'
    model = Book_shelf
    

class BookDetailsView(DetailView):
    template_name = 'details.html'
    model = Book_shelf

class CreateNewView(CreateView):
    template_name = 'create.html'
    model = Book_shelf
    fields = ['title' , 'author' , 'body']

class BookUpdateView(UpdateView):
    template_name = 'update.html'
    model = Book_shelf
    fields = ['title' , 'author' , 'body']

class BookDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Book_shelf
    fields = ['title' , 'author' , 'body']
    success_url = reverse_lazy('home')