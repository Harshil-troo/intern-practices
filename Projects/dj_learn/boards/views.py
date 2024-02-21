from django.shortcuts import render
from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def about(request):
    # do something...
    return render(request, 'about.html')

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})

def about_author(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_author.html', {'author_name': 'Simple Complex'})

def about_vitor(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_vitor.html', {'vitor_name': 'Simple Complex'})

def about_erica(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_erica.html', {'erica_name': 'Simple Complex'})

def privacy(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'privacy.html', {'privacy': 'Simple Complex'})

def board_topics(request,board_id):

    return render(request,'board_topics.html',{'boards_topics': 'Simple Complex'})